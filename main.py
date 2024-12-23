import os
import sys
import argparse

from steps.data_ingestion_step import data_ingestion_step

def main():
    """
    Main function to orchestrate the entire project.
    """
    parser = argparse.ArgumentParser(description= 'MLOps Project Main Entry Point.')
    parser.add_argument(
        '--task',
        choices= ['ingest', 'train', 'deploy'],
        help= "Task to execute: ingest | train | deploy"
    )

    args = parser.parse_args()

    if args.task == 'ingest':
        print("Starting data ingestion step...")
        data_ingestion_step()
    elif args.task == 'train':
        print("Training task is not implemented yet.")

    elif args.task == "deploy":
        print("Deployment task is not implemented yet.")

if __name__ == '__main__':
    main()