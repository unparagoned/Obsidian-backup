from ixbrl_ai.sample import DataSample
from networkx import display
import numpy as np
import polars as pl
from sklearn.calibration import LabelEncoder
from sklearn.model_selection import train_test_split

MAX_WORDS = 15
MIN_EXAMPLES = 350 
SEED = 42

def clean_field(dataset_pl: pl.DataFrame, feature: str, output_feature: str) -> pl.DataFrame:
    """Cleans the field

    Args:
        dataset_pl (pl.DataFrame): Dataset
        feature (str): Column name of feature to clean
        output_feature (str): Column name for the cleaned feature

    Returns:
        pl.DataFrame: Dataset including the cleaned feature
    """

    clean = (
        pl.col(feature)
        .str.to_lowercase()
        .str.strip_chars()
        .str.replace_all(r"\(|\)", "")
        .str.replace_all(r":", " ")
        .str.replace_all(r"\s+", " ")
        # .str.replace_all(r'\/', ' ') # this actually reduces performance
        .str.strip_chars()
    )

    return dataset_pl.with_columns(clean.alias(output_feature))


def canonicalize_field(dataset_pl: pl.DataFrame, feature: str, output_feature: str) -> pl.DataFrame:
    """Normalize has multiple meanings so use canonicalize
    Replace names, dates and numbers with standardised hubble_type value

    Args:
        dataset_pl (pl.DataFrame): Dataset
        feature (str): Column name of the feature
        output_feature (str): Column name for the canonical feature

    Returns:
        pl.DataFrame: Dataset including canonical feature
    """

    company_pattern = r".*(ltd|limited|plc|(public limited company)|(public limited)|llp|(limited liability partnership)|lp|(limited partnership)|co)\b"
    postcode_pattern = r"(?i)\b(?:GIR 0AA|(?:[A-Z]{1,2}\d[A-Z\d]?|\d[A-Z]{2})\s?\d[A-Z]{2})\b"
    date_pattern = r"(?:as\s+)?(?:(at|on|in|as)\s+)?\d{1,2}\w{0,2} \b(?:jan(?:uary)?|feb(?:ruary)?|mar(?:ch)?|apr(?:il)?|may|jun(?:e)?|jul(?:y)?|aug(?:ust)?|sep(?:t(?:ember)?)?|oct(?:ober)?|nov(?:ember)?|dec(?:ember)?)\b\s*\d{0,4}"

    canonicalize = (
        pl.col(feature)
        .str.replace(
            r"31.*(march|03).*1982", "hubble_date_1982_03_31"
        )  # Special date for tax so treat differently
        .str.replace_all(company_pattern, "hubble_company_name")
        .str.replace(postcode_pattern, "hubble_postcode")
        .str.replace_all(date_pattern, "hubble_date")
        .str.replace_all(r"(?:as\s+)?(?:(at|on|in|as)\s+)?\d+\w* \w+ \d{2,4}", "hubble_date")
        .str.replace_all(r"(?:as\s+)?(?:(at|on|in|as)\s+)?\d+[\s\/\-]\d+[\s\/\-]\d+", "hubble_date")
        .str.replace_all(r"[\d,\.]+(rd|st|nd|th|)", "hubble_number")
        .str.replace_all(r"(.* |^)(mr|ms).*", "hubble_name")
        .str.strip_chars()
    )

    return dataset_pl.with_columns(canonicalize.alias(output_feature))


def standardise_names(dataset_pl: pl.DataFrame, feature: str, label: str) -> pl.DataFrame:
    """Backup to ensure all names are replaced with hubble_name

    Args:
        dataset_pl (pl.DataFrame): Dataset
        feature (str): Column name of feature
        label (str): Column name of label

    Returns:
        pl.DataFrame: Dataset with standardised names
    """

    names = [
        "NameEntityOfficer",
        "NamedEntityOfficer",
        "NameDirector",
        "DirectorSigningFinancialStatements",
        "NameSeniorStatutoryAuditor",
        "NameOfEngagementPartner",
        "NameLLPMember",
        "NameTrustee",
        "NameGeneralPartner",
        "NameLimitedPartner",
        "NameAssociate",
        "NameAccountantResponsible",
    ]
    company_names = [
        "NameEntity",
        "EntityCurrentLegalOrRegisteredName",
        "NameEntityLawyersOrLegalAdvisersEntityTradingName",
        "NameOfReportingEntity",
        "NameAuditor",
        "NameSeniorStatutoryCharityAuditor",
        "NameEntityCharityAuditors",
        "NameIndividualAuditor",
        "NameEntityAuditors",
        "NameOfAuditFirm",
        "NameSubsidiary",
        "NameParent",
        "NameImmediateParent",
        "NameUltimateParent",
        "NameRelatedParty",
        "NameEntityAccountants",
        "NameControllingParty",
        "NameEntityBankers",
        "NameParentEntity",
        "NameOrDescriptionRelatedPartyIfNotDefinedByAnotherTag",
    ]

    return dataset_pl.with_columns(
        pl.when(pl.col(label).is_in(names))
        .then(pl.lit("hubble_name"))
        .when(pl.col(label).is_in(company_names))
        .then(pl.lit("hubble_company_name"))
        .otherwise(pl.col(feature))
        .alias(feature)
    )


def target_engineer(dataset_pl: pl.DataFrame, feature: str, label: str, output_label: str) -> pl.DataFrame:
    """Replace the xbrl_tags with the cleaned_description if it just contains hubble_
    If it's just a number, date or name then it's not enough to predict the tag, but creating our own target labels might help.

    Args:
        dataset_pl (pl.DataFrame): Dataset
        feature (str): Column name of feature
        label (str): Column name of label
        output_label (str): Column name to be used for canonical label

    Returns:
        pl.DataFrame: Dataset with canonical label
    """
    return dataset_pl.with_columns(
        pl.when(pl.col(feature).str.contains("^hubble_[a-z_]*$"))
        .then(pl.col(feature))
        .otherwise(pl.col(label))
        .alias(output_label)
    )


def set_min_examples(dataset_pl: pl.DataFrame, label: str = "canonical_label", examples: int = MIN_EXAMPLES) -> pl.DataFrame:
    """Filters by min examples

    Args:
        df (pl.DataFrame): Dataset
        label (str, optional): Column name of label to count over. Defaults to "canonical_label".
        examples (int, optional): Number of minimum examples. Defaults to MIN_EXAMPLES.

    Returns:
        pl.DataFrame: _description_
    """
    return dataset_pl.with_columns(
        pl.len().over("canonical_label").ge(examples).alias("min_examples")
    )


def filter_data(dataset_pl: pl.DataFrame) -> pl.DataFrame:
    """Filters out problematic data, too long, too short or null

    Args:
        dataset_pl (pl.DataFrame): Dataset

    Returns:
        pl.DataFrame: Filtered datasetI
    """
    return dataset_pl.filter(
        # less than 12 words in the description, don't use canonicalized description since that can be misleading with the editing
        pl.col("description").str.count_matches(r"\w+") <= MAX_WORDS,
        pl.col("canonical_description").str.len_chars() > 2,
        pl.col("canonical_description").is_not_null(),
    )


def filter_out_labels(dataset_pl: pl.DataFrame) -> pl.DataFrame:
    """Filters out specific labels that we aren't interested in like locations or principal activity

    Args:
        dataset_pl (pl.DataFrame): Dataset

    Returns:
        pl.DataFrame: Filtered Dataset
    """

    xbrl_concepts = [
        "DescriptionPrincipalActivities",
        "DescriptionActivity",
        "AddressLine1",
        "AddressEntityBankers",
        "AddressLine2",
        "AddressEntityCharityAuditors",
        "AddressLine3",
        "PrincipalLocation-CityOrTown",
        "NameOrLocationOfficePerformingAudit",
        "NameOrLocationAccountantsOffice",
    ]
    return dataset_pl.filter(~pl.col("canonical_label").is_in(xbrl_concepts))


def standardizeLabelFormat(dataset_pl: pl.DataFrame, label: str) -> pl.DataFrame:
    """Turns snake_case labels to CammelCase

    Args:
        dataset_pl (pl.DataFrame): Dataset
        label (str): Column name for the label

    Returns:
        pl.DataFrame: Dataset with with CammelCase labels
    """
    return dataset_pl.with_columns(
        pl.when(pl.col(label).str.contains("hubble_"))
        .then(pl.col(label).str.split("_").list.eval(pl.element().str.to_titlecase()).list.join(""))
        .otherwise(pl.col(label))
        .alias(label)
    )


def stratified_split(
    dataset_processed_pl: pl.DataFrame,
    label: str = "canonical_label",
    train_fraction: float = 0.8,
    test_fraction: float = 0.1,
) -> pl.DataFrame:
    """Adds split column saying if it belongs to train, best or holdout

    Args:
        dataset_processed_pl (pl.DataFrame): Dataset
        label (str, optional): Column name for the label. Defaults to "canonical_label".
        train_fraction (float, optional): Fraction of train. Defaults to 0.8.
        test_fraction (float, optional): Fraction of test. Defaults to 0.1.

    Returns:
        pl.DataFrame: Dataset with split column
    """

    min_examples = dataset_processed_pl["min_examples"].to_numpy()

    idx = np.arange(dataset_processed_pl.height)[min_examples]
    y = dataset_processed_pl.get_column(label).to_numpy()[min_examples]

    idx_train, idx_temp, y_train, y_temp = train_test_split(idx, y, test_size=(1 - train_fraction), stratify=y, random_state=SEED)

    idx_test, idx_holdout = train_test_split(idx_temp, test_size=0.5, stratify=y_temp, random_state=SEED)


    split = np.full(dataset_processed_pl.height, "excluded")
    split[min_examples] = "holdout"
    split[idx_train] = "train"
    split[idx_test] = "test"

    # Add a 5 pct colulm for faster BERT testing
    idx_5_pct, _ = train_test_split(
        idx_test,
        test_size=0.95,
        stratify=dataset_processed_pl[idx_test].get_column(label).to_numpy(),
        random_state=SEED,
    )
    
    test_5_pct = np.full(dataset_processed_pl.height, False)
    test_5_pct[idx_5_pct] = True

    return dataset_processed_pl.with_columns(
        pl.Series("split", split), 
        pl.Series("test_5_pct", test_5_pct),
        pl.Series("train", split == "train"),
        pl.Series("test", split == "test"),
        pl.Series("holdout", split == "holdout")
        )


def sample_split(
    dataset_split_pl: pl.DataFrame, feature: str = "canonical_description", label: str = "canonical_label"
) -> pl.DataFrame:
    """Adds columns for unique, 1%, 10%, 50% and 100% samples

    Args:
        df (pl.DataFrame): Dataset
        feature (str, optional): Column name of the feature. Defaults to "canonical_description".
        label (str, optional): Column name of the label. Defaults to "canonical_label".

    Returns:
        pl.DataFrame: Dataset with columns for sample types from DataSample
    """

    df = dataset_split_pl.drop("row_id", strict=False).with_row_index("row_id")

    train_pl = df.filter(pl.col("split") == "train")

    idx_train = train_pl.get_column("row_id").to_numpy()
    y = df[idx_train].get_column(label).to_numpy()

    def samples_bool(sample: DataSample, idx_rows: np.ndarray, y: np.ndarray, current_fraction: float | np.floating=1.0):
        if sample.fraction == 1:
            sample_array = np.full(df.height, False)
            sample_array[idx_rows] = True
            return sample_array, idx_rows

        if sample.fraction is None:
            return None, None

        test_fraction = (1 - sample.fraction/current_fraction)
        idx_sample, idx_not_sample = train_test_split(
            idx_rows,
            test_size=test_fraction,
            stratify=y,
            random_state=SEED,
        )
        sample_array = np.full(df.height, False)
        sample_array[idx_sample] = True
        return sample_array, idx_sample

    new_cols: list[pl.Series] = []

    idx_rows = idx_train
    current_fraction = 1.0
    for sample in DataSample:
        sample_array, idx_rows = samples_bool(sample, idx_rows, y, current_fraction)
        
        if sample_array is None:
            continue

        current_fraction = sample.fraction 

        new_cols.append(pl.Series(sample.label, sample_array))
        
        y = df[idx_rows].get_column(label).to_numpy()

    return df.with_columns(
        *new_cols,
        pl.when(pl.col("split") == "train")
        .then(pl.int_range(0, pl.len()).over(feature, label) == 0)
        .otherwise(True)
        .alias("sample_unique"),
    )


def add_sqrt_weight(dataset_sample_split_pl: pl.DataFrame) -> pl.DataFrame:
    """Add sqrt weigtings to make weigtings more balanced

    Args:
        dataset_sample_split_pl (pl.DataFrame): Dataset

    Returns:
        pl.DataFrame: Dataset
    """

    label_counts_pl = dataset_sample_split_pl["canonical_label"].value_counts()
    label_counts_pl = label_counts_pl.with_columns((1/pl.col("count").sqrt()).alias("sqrt_weight"))
    df = dataset_sample_split_pl.join(label_counts_pl, on="canonical_label")
    train_pl = df.filter(pl.col("split")=="train")
    probs = train_pl["sqrt_weight"]
    probs = probs / probs.sum()
    n = int(train_pl.height/100)
    indexes_1_pct = np.random.choice(train_pl.height, size=n, replace=False, p=probs)
    sample_rows_1_pct = train_pl[indexes_1_pct]["row_id"].to_numpy()

    n = int(10*train_pl.height/100)
    indexes_10_pct = np.random.choice(train_pl.height, size=n, replace=False, p=probs)
    sample_rows_10_pct = train_pl[indexes_10_pct]["row_id"].to_numpy()

    return dataset_sample_split_pl.with_columns(
        pl.col("row_id").is_in(sample_rows_1_pct).alias("sample_1_pct_sqrt_weight"),
        pl.col("row_id").is_in(sample_rows_10_pct).alias("sample_10_pct_sqrt_weight"))



def addLabels(dataset_sample_split_pl: pl.DataFrame) -> pl.DataFrame:
    """Adds column for canonical description and canonical label

    Args:
        dataset_pl (pl.DataFrame): Dataset  

    """
    le = LabelEncoder()
    labels = le.fit_transform(dataset_sample_split_pl.get_column("canonical_label"))
    return dataset_sample_split_pl.with_columns(pl.Series("label", labels))




# dataset_processed_pl = (
#     dataset_pl.pipe(clean_field, feature="description", output_feature="cleaned_description")
#     .pipe(canonicalize_field, feature="cleaned_description", output_feature="canonical_description")
#     .pipe(standardise_names, feature="canonical_description", label="xbrl_concept")
#     .pipe(
#         target_engineer, feature="canonical_description", label="xbrl_concept", output_label="canonical_label"
#     )
#     .pipe(standardizeLabelFormat, "canonical_label")
#     .pipe(filter_out_labels)
#     .pipe(filter_data)
#     .pipe(set_min_examples)
#     .drop("row_id", strict=False)
#     .with_row_index("row_id")
# )

# dataset_processed_pl

# dataset_split_pl = stratified_split(dataset_processed_pl)

# dataset_sample_split_pl = sample_split(dataset_split_pl)
# dataset_sample_split_pl = add_sqrt_weight(dataset_sample_split_pl)

# dataset_encoded_pl = addLabels(dataset_sample_split_pl)
# dataset_encoded_pl.write_parquet("data/canonicalized_split_v13.parquet")

