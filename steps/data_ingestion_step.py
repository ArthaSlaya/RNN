import os
import sys

# Add the project root directory to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from src.data_ingestion import DataIngestion

def process_train1(file_name: str, ingestion: DataIngestion) -> None:
    """
    Processes the first training file.
    """
    df = ingestion.load_data(file_name= file_name)
    print(f"Processing train file: {file_name}")

    # Perform train1-specific processing
    if 'sentiment' in df.columns:
        df = df.dropna(subset= ['sentiment']) # Example: Drop rows without sentiment
    
    # Save processed train file
    processed_file_name = f"processed_{file_name}"
    ingestion.save_data(df, processed_file_name)

def process_train2(file_name: str, ingestion: DataIngestion):
    """
    Processes the second training file.
    """
    df = ingestion.load_data(file_name)
    print(f"Processing train file: {file_name}")
    
    # Perform train2-specific processing
    if "polarity of tweet" in df.columns:
        df = df.dropna(subset=["polarity of tweet"])  # Example: Drop rows without polarity
    
    # Save processed train file
    processed_file_name = f"processed_{file_name}"
    ingestion.save_data(df, processed_file_name)

def process_test1(file_name: str, ingestion: DataIngestion):
    """
    Processes the first test file.
    """
    df = ingestion.load_data(file_name)
    print(f"Processing test file: {file_name}")
    
    # Perform test1-specific processing
    # Example: Custom logic for test1 file
    df = df.fillna("Unknown")  # Example: Fill missing values
    
    # Save processed test file
    processed_file_name = f"processed_{file_name}"
    ingestion.save_data(df, processed_file_name)

def process_test2(file_name: str, ingestion: DataIngestion):
    """
    Processes the second test file.
    """
    df = ingestion.load_data(file_name)
    print(f"Processing test file: {file_name}")
    
    # Perform test2-specific processing
    # Example: Custom logic for test2 file
    if "query" in df.columns:
        df = df.drop(columns=["query"])  # Example: Drop unnecessary columns
    
    # Save processed test file
    processed_file_name = f"processed_{file_name}"
    ingestion.save_data(df, processed_file_name)

def data_ingestion_step() -> None:
    """
    Performs the data ingestion step in the pipeline.
    """
    raw_data_path = './data/archive'

    raw_train_file_name1 = 'training.1600000.processed.noemoticon.csv'
    raw_train_file_name2 = 'train.csv'
    train_files = [raw_train_file_name1, raw_train_file_name2]

    raw_test_file_name1 = 'testdata.manual.2009.06.14.csv'
    raw_test_file_name2 = 'test.csv'
    test_files = [raw_test_file_name1, raw_test_file_name2]

    processed_data_path = './data/processed'

    # Initialize DataIngestion
    ingestion = DataIngestion(raw_data_path= raw_data_path, processed_data_path= processed_data_path)

    # Process train files
    process_train1(train_files[0], ingestion)
    process_train2(train_files[1], ingestion)

    # Process test files
    process_test1(test_files[0], ingestion)
    process_test2(test_files[1], ingestion)