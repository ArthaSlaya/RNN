import os
import sys
import argparse

from scripts.run_data_ingestion_pipeline import run_data_ingestion_pipeline
from steps.preprocessing_step import preprocessing_step
from steps.advanced_preprocessing_step import advanced_preprocessing_step

project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_root)

print(sys.path)

def main():
    """
    Main function to orchestrate the entire project.
    """
    parser = argparse.ArgumentParser(description= 'MLOps Project Main Entry Point.')
    parser.add_argument(
        '--task',
        choices= ['ingest', 'preprocess', 'advanced_preprocess', 'train', 'deploy'],
        help= (
            "Task to execute:\n"
            "  ingest              - Perform data ingestion step.\n"
            "  preprocess          - Preprocess the raw data for modeling.\n"
            "  advanced_preprocess - Apply additional transformations to processed data.\n"
            "  train               - Train the machine learning model (not yet implemented).\n"
            "  deploy              - Deploy the trained model (not yet implemented)."
        )
    )

    args = parser.parse_args()

    if args.task == 'ingest':
        print("Starting data ingestion step...")
        run_data_ingestion_pipeline()

    elif args.task == 'preprocess':
        print("Starting data preprocessing step...")
        preprocessing_step()

    elif args.task == 'advanced_preprocess':
        print("Starting advanced preprocessing step...")
        advanced_preprocessing_step()

    elif args.task == 'train':
        print("Training task is not implemented yet.")

    elif args.task == "deploy":
        print("Deployment task is not implemented yet.")

if __name__ == '__main__':
    main()