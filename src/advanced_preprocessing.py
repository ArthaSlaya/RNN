import pandas as pd
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import re

class AdvancedPreprocessing:
    def __init__(self):
        self.stemmer = PorterStemmer()
        self.stop_words = set(stopwords.words('english'))

    @staticmethod
    def remove_user_mentions(text: str) -> str:
        """
        Removes `@user` mentions from the text.
        """
        return re.sub(r"@\w+", "", text)
    
    @staticmethod
    def remove_stopwords(text: str, stop_words: set) -> str:
        """
        Removes stopwords from the text.
        """
        words = text.split()
        filtered_words = [word for word in words if word not in stop_words]
        return " ".join(filtered_words)
    
    def apply_stemming(self, text: str) -> str:
        """
        Applies stemming to the text.
        """
        words = text.split()
        stemmed_words = [self.stemmer.stem(word) for word in words]
        return " ".join(stemmed_words)
    
    def clean_text(self, text: str) -> str:
        """
        Cleans the text by:
        - Lowercasing.
        - Removing URLs, special characters, and extra whitespace.
        """
        if not isinstance(text, str):
            return ""
        
        text = text.lower()  # Convert to lowercase
        text = re.sub(r"http\S+|www\S+|https\S+", "", text)  # Remove URLs
        text = self.remove_user_mentions(text)  # Remove user mentions
        text = re.sub(r"[^a-zA-Z\s]", "", text)  # Remove special characters and numbers
        text = re.sub(r"\s+", " ", text).strip()  # Remove extra whitespace
        return text
    
    def preprocess(self, df: pd.DataFrame, text_col: str) -> pd.DataFrame:
        """
        Applies the complete preprocessing pipeline:
        - Cleans text.
        - Removes stopwords.
        - Applies stemming.
        """
        print(f"Applying advanced preprocessing to column: {text_col}")

        # Clean text
        df[text_col] = df[text_col].apply(self.clean_text)

        # Remove stopwords
        df[text_col] = df[text_col].apply(lambda x: self.remove_stopwords(x, self.stop_words))

        # Apply stemming
        df[text_col] = df[text_col].apply(self.apply_stemming)

        return df