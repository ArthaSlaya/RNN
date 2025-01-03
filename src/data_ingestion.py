import pandas as pd
import os

class DataIngestion:
    def __init__(self, raw_data_path, processed_data_path):
        """
        Initializes the DataIngestion class.

        Parameters:
        - raw_data_path: Path to the directory containing raw data files.
        - processed_data_path: Path to the directory to save processed data files.
        """
        self.raw_data_path = raw_data_path
        self.processed_data_path = processed_data_path

    def load_data(self, file_name: str) -> pd.DataFrame:
        """
        Loads data from a CSV file.

        Parameters:
        - file_name: Name of the raw data file.

        Returns:
        - pd.DataFrame: Loaded dataset.
        """
        file_path = os.path.join(self.raw_data_path, file_name)
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        print(f"Loading data from {file_path}...")
        df = pd.read_csv(file_path, encoding="ISO-8859-1")
        print(f"Data loaded with shape: {df.shape}")
        return df

    def save_data(self, df: pd.DataFrame, file_name: str):
        """
        Saves data to a CSV file.

        Parameters:
        - df: DataFrame to save.
        - file_name: Name of the processed data file.
        """
        os.makedirs(self.processed_data_path, exist_ok=True)
        file_path = os.path.join(self.processed_data_path, file_name)
        print(f"Saving data to {file_path}...")
        df.to_csv(file_path, index=False)
        print("Data saved successfully.")

def load_and_save(file_name: str, ingestion: DataIngestion) -> None:
    """
    Loads a dataset and saves it as-is.

    Parameters:
    - file_name: Name of the raw data file.
    - ingestion: Instance of the DataIngestion class.
    """
    # Load the dataset
    df = ingestion.load_data(file_name= file_name)

    # Define the processed file name
    processed_filename = f"processed_{file_name}"

    # Save the dataset
    ingestion.save_data(df= df, file_name= processed_filename)