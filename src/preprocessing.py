import pandas as pd
import re

class Preprocessing:
    def __init__(self):
        pass

    @staticmethod
    def clean_text(text: str) -> str:
        """
        Cleans text by removing URLs, special characters, and extra whitespace.

        Parameters:
        - text: Input text string.

        Returns:
        - Cleaned text string.
        """

        if not isinstance(text, str):
            return ""
        text = text.lower()  # Convert to lowercase
        text = re.sub(r"http\S+|www\S+|https\S+", "", text)  # Remove URLs
        text = re.sub(r"[^a-zA-Z\s]", "", text)  # Remove special characters and numbers
        text = re.sub(r"\s+", " ", text).strip()  # Remove extra whitespace
        return text
    
    def preprocess_dataset(self, df: pd.DataFrame, text_col: str, target_col: str, polarity_map: dict = None):
        """
        Cleans and filters the dataset. Optionally maps polarity to labels.

        Parameters:
        - df: Input dataframe.
        - text_col: Name of the column containing text data.
        - target_col: Name of the column containing target labels.
        - polarity_map: Mapping of polarity values to labels.

        Returns:
        - Preprocessed dataframe with selected columns.
        """
        # Clean text
        print(f"Cleaning text column: {text_col}")
        df[text_col] = df[text_col].apply(self.clean_text)

        # Map polarity if a mapping is provided
        if polarity_map:
            df[target_col] = df[target_col].map(polarity_map)

        # Select relevant columns
        df = df[[text_col, target_col]].dropna()

        return df