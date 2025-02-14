import os
import pandas as pd
from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize

class TextVectorizer:
    """
    Class for text vectorization using Word2Vec from Gensim.
    
    This class:
    - Trains a Word2Vec model on the input text data.
    - Transforms text into numerical vectors.
    - Outputs a DataFrame with vectorized features for each text.
    """
    def __init__(self ,vector_size= 100, window= 5, min_count= 2, workers= 4):
        """
        Initializes the Word2Vec vectorizer with the provided hyperparameters.
        
        Args:
            vector_size (int): Dimensionality of the feature vectors.
            window (int): Maximum distance between current and predicted word.
            min_count (int): Ignores words with total frequency lower than this.
            workers (int): Number of worker threads to train the model.
        """
        self.vector_size = vector_size
        self.window = window
        self.min_count = min_count
        self.workers = workers

    def train_word2vec(self, sentences):
        """
        Trains a Word2Vec model on tokenized sentences.
        
        Args:
            sentences (list of list): Tokenized sentences.
        
        Returns:
            Word2Vec: Trained Word2Vec model.
        """
        print("Training Word2Vec model...")
        model = Word2Vec(
            sentences= sentences,
            vector_size= self.vector_size,
            window= self.window,
            min_count= self.min_count,
            workers= self.workers
        )

        return model
    
    def vectorize_data(self, df, text_col):
        """
        Tokenizes text data, trains Word2Vec, and applies vectorization.
        
        Args:
            df (pd.DataFrame): DataFrame containing text data.
            text_col (str): Column name containing text.
        
        Returns:
            pd.DataFrame: DataFrame with vectorized text features.
        """
        # Tokenize text
        tokenized_sentences = df[text_col].apply(word_tokenize).tolist()

        # Train Word2Vec model
        model = self.train_word2vec(tokenized_sentences)

        # Generate vector for each text by averaging word vectors
        def vectorize_text(tokens):
            vectors = [model.wv[word] for word in tokens if word in model.wv]
            if len(vectors) == 0:
                return [0] * self.vector_size
            return list(sum(vectors) / len(vectors))
        
        print("Applying vectorization...")
        df['vectorized_text'] = df[text_col].apply(lambda x: vectorize_text(word_tokenize(x)))

        # Split vector columns
        vectorized_columns = pd.DataFrame(df['vectorized_text'].to_list(), columns= [f'vec_{i}' for i in self.vector_size])
        return pd.concat([df.drop(columns= ['vectorized_text']), vectorized_columns], axis= 1)
