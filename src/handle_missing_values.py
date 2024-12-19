import pandas as pd

class MissingValuesHandler:
    def __init__(self, num_strategy: str= 'mean', text_strategy: str = 'Unknown') -> None:
        """
        Initialize the MissingValuesHandler.

        Parameters:
        - num_strategy: Strategy for imputing missing values in numerical columns ("mean", "median", "mode", or "drop").
        - text_strategy: Strategy for imputing missing values in text columns ("unknown", "mode", or "drop").
        """
        self.num_strategy = num_strategy
        self.text_strategy = text_strategy

    def handle_missing_values(self, df: pd.DataFrame, num_columns: list= None, text_columns: list = None) -> pd.DataFrame:
        """
        Handle missing values in the given DataFrame.

        Parameters:
        - df: The input DataFrame.
        - num_columns: List of numerical columns to handle. If None, detects all numerical columns automatically.
        - text_columns: List of text columns to handle. If None, detects all text columns automatically.

        Returns:
        - df: The DataFrame with missing values handled.
        """
        # Handle numerical columns
        if num_columns is None:
            num_columns = df.select_dtypes(include=["number"]).columns

        for column in num_columns:
            if df[column].isnull().sum() > 0:
                if self.num_strategy == "mean":
                    df[column] = df[column].fillna(df[column].mean())
                elif self.num_strategy == "median":
                    df[column] = df[column].fillna(df[column].median())
                elif self.num_strategy == "mode":
                    df[column] = df[column].fillna(df[column].mode()[0])
                elif self.num_strategy == "drop":
                    df = df.dropna(subset=[column])
                else:
                    raise ValueError(f"Unknown numerical strategy: {self.num_strategy}")

        # Handle text columns
        if text_columns is None:
            text_columns = df.select_dtypes(include=["object"]).columns

        for column in text_columns:
            if df[column].isnull().sum() > 0:
                if self.text_strategy == "unknown":
                    df[column] = df[column].fillna("Unknown")
                elif self.text_strategy == "mode":
                    df[column] = df[column].fillna(df[column].mode()[0])
                elif self.text_strategy == "drop":
                    df = df.dropna(subset=[column])
                else:
                    raise ValueError(f"Unknown text strategy: {self.text_strategy}")

        return df