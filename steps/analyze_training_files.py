import pandas as pd
import os

def analyze_training_files():
    """
    Loads and analyzes training files to determine column relevance.
    """

    # Paths
    raw_data_path = "./data/archive"
    train_files = [
        "training.1600000.processed.noemoticon.csv",
        "train.csv"
    ]

    for file_name in train_files:
        file_path = os.path.join(raw_data_path, file_name)
        if not os.path.exists(path= file_path):
            print(f"File not found: {file_path}")
            continue

        print(f"\nAnalyzing file: {file_name}")
        df = pd.read_csv(file_path, encoding="ISO-8859-1")
        print(f"Shape: {df.shape}")
        print("Columns:")
        print(df.columns)
        print("\nSample Data:")
        print(df.head())
        print("\nMissing Values:")
        print(df.isnull().sum())

analyze_training_files()