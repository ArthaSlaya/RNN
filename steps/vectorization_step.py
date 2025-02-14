import os
import pandas as pd
from zenml.steps import step
from src.vectorization import TextVectorizer

@step
def vectorization_step():
    """
    ZenML step to apply text vectorization on processed datasets.
    
    This step:
    1. Loads processed training and test datasets.
    2. Applies Word2Vec vectorization.
    3. Saves the vectorized data for training models.
    
    Outputs:
    - `./data/vectorized/vectorized_train.csv`
    - `./data/vectorized/vectorized_test.csv`
    """
    processed_data_path = './data/tranformed'
    vectorized_data_path = './data/vectorized'

    # Load the transfrmed data
    train_data = pd.read_csv(os.path.join(processed_data_path, 'transformed_combined_train.csv'))
    test_data = pd.read_csv(os.path.join(processed_data_path, 'transformed_combined_test.csv'))

    # Initialize the vectorizer
    vectorizer = TextVectorizer()

    # Apply vectorization
    print("Vectorizing training data...")
    vectorized_train = vectorizer.vectorize_data(train_data, text_col= 'text')

    print("Vectorizing test data...")
    vectorized_test = vectorizer.vectorize_data(test_data, text_col= 'text')

    # Save vectorized data
    os.makedirs(vectorized_data_path, exist_ok= True)
    vectorized_train.to_csv(os.path.join(vectorized_data_path, 'vectorized_train.csv'), index= False)
    vectorized_test.to_csv(os.path.join(vectorized_data_path, 'vectorized_test.csv'), index= False)
    print("Vectorized data saved successfully.")
