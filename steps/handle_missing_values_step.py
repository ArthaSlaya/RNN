from src.handle_missing_values import MissingValuesHandler
import pandas as pd
import os

def handle_missing_values_step():
    """
    Handles missing values in the processed datasets.
    """
    processed_data_path = "./data/processed"
    output_data_path = "./data/processed_with_no_missing"

    os.makedirs(output_data_path, exist_ok= True)

    # Define the datasets to process
    datasets = [
        "processed_train.csv", 
        "processed_training.1600000.processed.noemoticon.csv", 
        "processed_test.csv", 
        "processed_testdata.manual.2009.06.14.csv"
        ]
    
    # Initialize the handler
    handler = MissingValuesHandler(num_strategy="mean", text_strategy= 'mode')

    for dataset in datasets:
        file_path = os.path.join(processed_data_path, dataset)
        if not os.path.exists(file_path):
            print(f'File not found: {file_path}')
            continue

        print(f'Handling missing values for {dataset}')
        df = pd.read_csv(file_path)

        # Identify numerical and text columns
        num_columns = df.select_dtypes(include= ['number']).columns.to_list()
        text_columns = df.select_dtypes(include= ['object']).columns.to_list()

        # Apply missing value handling
        df = handler.handle_missing_values(df, num_columns= num_columns, text_columns= text_columns)

        # Save the processed datase
        output_file_path = os.path.join(output_data_path, dataset)
        df.to_csv(path_or_buf= output_file_path, index= False)
        print(f'Saved processed file: {output_file_path}')