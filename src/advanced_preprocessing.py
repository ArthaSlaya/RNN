import os
import nltk

# Set up custom NLTK data directory
# 1. Create a Custom NLTK Data Directory
nltk_data_dir = os.path.join(os.getcwd(), 'nltk_data')

# Creates the nltk_data folder if it doesn't exist.
# The exist_ok=True ensures no error is raised if the folder already exists.
os.makedirs(name= nltk_data_dir, exist_ok= True)

# 2. Add the Directory to NLTK's Data Search Path
# NLTK has a list of directories where it looks for its resources (e.g., stopwords).
# nltk.data.path.append(nltk_data_dir) tells NLTK to also check the newly created nltk_data directory for resources.
nltk.data.path.append(nltk_data_dir)

# 3. Download the Stopwords Resource
# Downloads the stopwords resource and saves it in the nltk_data directory you just created.
nltk.download('stopwords', download_dir= nltk_data_dir)

import re
import emoji
import pandas as pd
from contractions import fix
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

class AdvancedPreprocessing:
    def __init__(self):
        self.stemmer = PorterStemmer()
        self.lemmatizer = WordNetLemmatizer()
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
    
    def apply_lemmatization(self, text: str) -> str:
        """
        Applies lemmatization to the text.
        """
        words = text.split()
        lemmatized_words = [self.lemmatizer.lemmatize(word= word) for word in words]
        return " ".join(lemmatized_words)
    
    @staticmethod
    def correct_spelling(text: str) -> str:
        """
        Corrects spelling in the text.
        """
        return str(TextBlob(text= text).correct())
    
    @staticmethod
    def expand_contraction(text: str) -> str:
        """
        Expands contractions in the text.
        """
        return fix(text)
    
    @staticmethod
    def remove_empjis(text: str) -> str:
        """
        Removes emojis from the text.
        """
        return emoji.replace_emoji(string= text, replace= '')
    
    def clean_text(self, text: str) -> str:
        """
        Cleans the text by:
        - Lowercasing.
        - Removing URLs, special characters, and extra whitespace.
        - Expanding contractions.
        """
        if not isinstance(text, str):
            return ""
        
        text = text.lower()  # Convert to lowercase
        text = self.expand_contraction(text= text) # Expand contractions
        text = re.sub(r"http\S+|www\S+|https\S+", "", text)  # Remove URLs
        text = self.remove_user_mentions(text)  # Remove user mentions
        text = self.remove_empjis(text= text) # Remove emojis
        text = re.sub(r"[^a-zA-Z\s]", "", text)  # Remove special characters and numbers
        text = re.sub(r"\s+", " ", text).strip()  # Remove extra whitespace
        return text
    
    def preprocess(self, df: pd.DataFrame, text_col: str) -> pd.DataFrame:
        """
        Applies the complete preprocessing pipeline:
        - Cleans text.
        - Removes stopwords.
        - Applies stemming or lemmatization.
        - Corrects spelling (optional).
        """
        print(f"Applying advanced preprocessing to column: {text_col}")

        # Clean text
        df[text_col] = df[text_col].apply(self.clean_text)

        # Remove stopwords
        df[text_col] = df[text_col].apply(lambda x: self.remove_stopwords(x, self.stop_words))

        # Apply stemming
        df[text_col] = df[text_col].apply(self.apply_stemming)

        # Apply stemming
        df[text_col] = df[text_col].apply(self.apply_lemmatization)

        # Correct spelling
        df[text_col] = df[text_col].apply(self.correct_spelling)

        return df