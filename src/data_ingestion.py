import pandas as pd
import os

class DataIngestion:
    def __init__(self, raw_data_path, processed_data_path):
        self.raw_data_path = raw_data_path
        self.processed_data_path = processed_data_path

    def load_data(self, file_name: str) -> pd.DataFrame:
        """
        Loads data from a CSV file.

        Parameters:
        - file_name: Name of the raw data file.

        Returns:
        - df: Loaded DataFrame.
        """
        file_path = os.path.join(self.raw_data_path, file_name)
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        print(f"Loading data from {file_path}...")

        df = pd.read_csv(file_path, encoding= 'ISO-8859-1')
        print(f"Data loaded with shape: {df.shape}")
        return df

    def save_data(self, df: pd.DataFrame, file_name: str):
        """
        Saves processed data to a CSV file.

        Parameters:
        - df: DataFrame to save.
        - file_name: Name of the processed data file.
        """
        os.makedirs(self.processed_data_path, exist_ok=True)
        file_path = os.path.join(self.processed_data_path, file_name)
        print(f"Saving processed data to {file_path}...")
        df.to_csv(file_path, index=False)
        print("Data saved successfully.")
