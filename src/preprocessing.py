import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Basic cleaning:
    - drop duplicates
    - handle missing values
    - convert date if needed
    """
    df = df.copy()
    df = df.drop_duplicates()

    # Example: fill or remove missing values depending on project choice
    missing_threshold = 0.5
    df = df.loc[:, df.isnull().mean() < missing_threshold]

    df = df.dropna(subset=["TotalPremium", "TotalClaims"])

    return df