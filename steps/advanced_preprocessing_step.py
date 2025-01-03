import os
import sys

# Add the project root directory to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from src.advanced_preprocessing import AdvancedPreprocessing
import pandas as pd

def advanced_preprocessing_step():
    """
    Task: Load processed data, apply advanced preprocessing methods, and save results.
    """
    processed_data_path = "./data/processed"
    transformed_data_path = "./data/transformed"

    # Initialize AdvancedPreprocessing
    processor = AdvancedPreprocessing()

    # List of processed files to load and transform
    files_to_process = [
        {"file": "combined_train.csv", "text_col": "text"},
        {"file": "combined_test.csv", "text_col": "text"},
    ]

    for file_info in files_to_process:
        file_name = file_info["file"]
        text_col = file_info["text_col"]

        file_path = os.path.join(processed_data_path, file_name)
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            continue

        print(f"\nLoading processed file: {file_name}")
        df = pd.read_csv(file_path)

        # Apply advanced preprocessing transformations
        transformed_df = processor.preprocess(df, text_col)

        # Save the transformed data
        os.makedirs(transformed_data_path, exist_ok=True)
        transformed_file_path = os.path.join(transformed_data_path, f"transformed_{file_name}")
        transformed_df.to_csv(transformed_file_path, index=False)
        print(f"Transformed data saved to: {transformed_file_path}")
