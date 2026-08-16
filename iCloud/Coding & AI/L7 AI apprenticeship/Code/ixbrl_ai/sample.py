from enum import Enum

class DataSample(Enum):
    sample_100_pct = ("sample_100_pct", 1)
    sample_50_pct = ("sample_50_pct", 0.5)
    sample_10_pct = ("sample_10_pct", 0.1)
    sample_1_pct = ("sample_1_pct", 0.01)
    sample_unique = ("sample_unique", None)
    sample_1_pct_sqrt_weight = ("sample_1_pct_sqrt_weight", None)
    sample_10_pct_sqrt_weight = ("sample_10_pct_sqrt_weight", None)
    sample_50_pct_sqrt_weight = ("sample_50_pct_sqrt_weight", None)


    def __init__(self, label:str, fraction: float | None):
        self.label = label
        self.fraction = fraction
