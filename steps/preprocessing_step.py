import os
import sys
import pandas as pd

from src.preprocessing import Preprocessing

def preprocessing_step():
    """
    Task: Preprocess training datasets.
    """
    raw_data_path = "./data/archive"
    processed_data_path = "./data/processed"

    # List of files to preprocess with column mappings
    files_to_process = [
        # Training datasets
        {
            "file": "training.1600000.processed.noemoticon.csv",
            "text_col": "text of the tweet\xa0",
            "target_col": "polarity of tweet\xa0",
            "polarity_map": {0: "negative", 4: "positive"},
        },
        {
            "file": "train.csv",
            "text_col": "text",
            "target_col": "sentiment",
            "polarity_map": None,  # Already labeled as negative, neutral, positive
        },
        # Test datasets
        {
            "file": "testdata.manual.2009.06.14.csv",
            "text_col": "text of the tweet\xa0",
            "target_col": "polarity of tweet\xa0",
            "polarity_map": {0: "negative", 4: "positive"},
        },
        {
            "file": "test.csv",
            "text_col": "text",
            "target_col": "sentiment",
            "polarity_map": None,  # Already labeled as negative, neutral, positive
        },
    ]

    # Initialize Preprocessing
    processor = Preprocessing()

    for train_file in files_to_process:
        file_name = train_file["file"]
        text_col = train_file["text_col"]
        target_col = train_file["target_col"]
        polarity_map = train_file["polarity_map"]

        file_path = os.path.join(raw_data_path, file_name)
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            continue

        print(f"\nProcessing file: {file_name}")
        df = pd.read_csv(file_path, encoding="ISO-8859-1")

        # the test file (testdata.manual.2009.06.14) didnt have column names
        # So we capture the columnnames from the train file(training.1600000.processed.noemoticon) to assign them to the test file
        if file_name == 'training.1600000.processed.noemoticon.csv':
            cols = df.columns
        elif file_name == 'testdata.manual.2009.06.14.csv':
            df.columns = cols

        # Normalize column names
        df.columns = df.columns.str.strip().str.lower()

        # Update column names to match normalized DataFrame
        text_col = text_col.strip().lower()
        target_col = target_col.strip().lower()

        # Preprocess the dataset
        processed_df = processor.preprocess_dataset(df, text_col, target_col, polarity_map)

        # Save the processed data
        os.makedirs(processed_data_path, exist_ok=True)
        processed_file_path = os.path.join(processed_data_path, f"processed_{file_name}")
        processed_df.to_csv(processed_file_path, index=False)
        print(f"Processed data saved to: {processed_file_path}")