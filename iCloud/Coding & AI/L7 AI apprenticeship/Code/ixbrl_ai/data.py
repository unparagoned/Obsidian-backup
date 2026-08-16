from typing import Tuple

import polars as pl 

from .sample import DataSample


def get_split(dataset_pl: pl.DataFrame, subset: DataSample) -> Tuple[pl.DataFrame, pl.DataFrame, pl.DataFrame]:
    """Filters to train, test, and holdout splits

    Args:
        dataset_df (pl.DataFrame): Dataset
        subset (DataSample): A subset type which is a sample or full dataset

    Returns:
        Tuple[pl.DataFrame, pl.DataFrame, pl.DataFrame]: train, test holdout
    """

    return (
        dataset_pl.filter(pl.col(subset.label), pl.col("split") == "train"),
        dataset_pl.filter(pl.col("split") == "test"),
        dataset_pl.filter(pl.col("split") == "holdout"),
    )