import os
import sys
import logging
import pandas as pd
from zenml.steps import step
from concurrent.futures import ThreadPoolExecutor

# Add the project root directory to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from src.advanced_preprocessing import AdvancedPreprocessing

# Logging Format Explanation:
# Components of the Format String:
# %(asctime)s:
#   - Includes the timestamp of when the log message was created.
#   - Default format: YYYY-MM-DD HH:MM:SS,ms (e.g., 2025-01-18 15:45:32,123).
#   - The format can be customized using the `datefmt` parameter.
# %(levelname)s:
#   - Represents the logging level of the message.
#   - Possible values: DEBUG, INFO, WARNING, ERROR, CRITICAL.
#   - Helps categorize the importance or severity of log messages.
# %(message)s:
#   - Contains the actual log message.
#   - This is the string passed to the logging methods (e.g., logging.info("This is a log message.")).

# -------------------------------------------------------------------------------
# | Placeholder      | Description                                        | Example                     |
# -------------------------------------------------------------------------------
# | %(asctime)s      | Time of log entry creation                         | 2025-01-18 15:45:32,123     |
# | %(levelname)s    | Logging level                                      | INFO, ERROR                 |
# | %(message)s      | The log message                                    | Processing started.         |
# | %(name)s         | Logger's name                                      | root                        |
# | %(filename)s     | Filename where the log entry was created           | script.py                   |
# | %(lineno)d       | Line number in the source file                     | 42                          |
# | %(threadName)s   | Name of the thread that generated the log          | MainThread                  |
# | %(module)s       | Name of the module where the log entry originated  | script                      |
# -------------------------------------------------------------------------------

# Set up logging
logging.basicConfig(level= logging.INFO, format= '%(asctime)s - %(levelname)s - %(message)s')

@step(enable_cache= False)
def advanced_preprocessing_step():
    """
    Task: Load processed data, apply advanced preprocessing methods, and save results.
    """
    print("Executing the advanced preprocessing step.")
    processed_data_path = "./data/processed"
    transformed_data_path = "./data/transformed"

    # Initialize AdvancedPreprocessing
    processor = AdvancedPreprocessing()

    # List of processed files to load and transform
    files_to_process = [
        {"file": "combined_train.csv", "text_col": "text"},
        {"file": "combined_test.csv", "text_col": "text"},
    ]

    # Ensure there are files to process
    if not files_to_process:
        logging.warning("No files to process. Exiting.")
        return
    
    def process_file(file_info):
        """
        Process a single file: apply preprocessing and save the result.
        """
        file_name = file_info['file']
        text_col = file_info['text_col']
        file_path = os.path.join(processed_data_path, file_name)

        try:
            # Check if the file exists
            if not os.path.exists(file_path):
                logging.warning(f"File not found: {file_path}")
                return
            
            # Load the data
            logging.info(f"Loading processed file: {file_name}")
            df = pd.read_csv(file_path)

            # Check if the required column exists
            if text_col not in df.columns:
                logging.warning(f"Column '{text_col}' not found in {file_name}. Skipping.")
                return
            
            # Apply preprocessing
            logging.info(f"Applying preprocessing to column '{text_col}' in {file_name}.")
            transformed_df = processor.preprocess(df= df, text_col= text_col)

            # Save the transformed data
            os.makedirs(transformed_data_path, exist_ok= True)
            transformed_file_path = os.path.join(transformed_data_path, f"transformed_{file_name}")
            transformed_df.to_csv(transformed_file_path, index= False)
            logging.info(f"Transformed data saved to: {transformed_file_path}")

        except Exception as e:
            logging.error(f"Error processing file {file_name}: {e}")

    # Use ThreadPoolExecutor for parallel processing
    with ThreadPoolExecutor() as executor:
        executor.map(process_file, files_to_process)