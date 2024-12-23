import os
import sys

from src.data_ingestion import DataIngestion

def load_and_save(file_name: str, ingestion: DataIngestion) -> None:
    """
    Loads a dataset and saves it as-is.
    """
    df = ingestion.load_data(file_name= file_name)

    processed_filename = f"processed_{file_name}"
    ingestion.save_data(df, processed_filename)


def data_ingestion_step():
    """
    Handles data ingestion for all datasets.
    """
    raw_data_path = "./data/archive"
    processed_data_path = "./data/processed"

    # List of raw files to ingest
    file_names = [
        "training.1600000.processed.noemoticon.csv",
        "train.csv",
        "testdata.manual.2009.06.14.csv",
        "test.csv",
    ]

    # Initialize the DataIngestion class
    ingestion = DataIngestion(raw_data_path= raw_data_path, processed_data_path= processed_data_path)

    # Load and save each file
    for file_name in file_names:
        print(f"\nProcessing file: {file_name}")
        df = ingestion.load_data(file_name= file_name)
        processed_file_name = f"processed_{file_name}"
        ingestion.save_data(df= df, file_name= processed_file_name)


    