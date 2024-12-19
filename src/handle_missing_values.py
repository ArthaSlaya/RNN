import pandas as pd

class MissingValuesHandler:
    def __init__(self, strategy: str= 'mean') -> None:
        """
        Initialize the MissingValuesHandler.

        Parameters:
        - strategy: Strategy for imputing missing values ("mean", "median", "mode", or "drop").
        """
        self.strategy = strategy

    def handle_missing_values(self, df: pd.DataFrame, columns: list= None) -> pd.DataFrame:
        """
        Handle missing values in the given DataFrame.

        Parameters:
        - df: The input DataFrame.
        - columns: List of columns to handle missing values. If None, all columns will be handled.

        Returns:
        - df: The DataFrame with missing values handled.
        """
        if columns is None:
            columns = df.columns

        for column in columns:
            if df[column].isnull().sum() > 0:
                if self.strategy == "mean":
                    df[column] = df[column].fillna(df[column].mean())
                elif self.strategy == "median":
                    df[column] = df[column].fillna(df[column].median())
                elif self.strategy == "mode":
                    df[column] = df[column].fillna(df[column].mode()[0])
                elif self.strategy == "drop":
                    df = df.dropna(subset=[column])
                else:
                    raise ValueError(f"Unknown strategy: {self.strategy}")
                
        return df