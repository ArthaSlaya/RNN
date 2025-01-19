import os
import sys
from zenml.steps import step
import dvc.api

from src.data_ingestion import DataIngestion, load_and_save

@step
def data_ingestion_step() -> None:
    """
    Step: Handles data ingestion for all datasets using the load_and_save function and tracks them with DVC.
    """
    print("Ingesting data...")
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
        load_and_save(file_name= file_name, ingestion= ingestion)

    # Track raw and processed data with DVC
    print(f'\nTracking raw and processed data with DVC...')
    os.system('dvc add data/archive')
    os.system('dvc add data/processed')
    os.system('git add data/archive.dvc data/processed.dvc .gitignore')
    os.system("git commit -m 'Track raw and procesed data with DVC'")