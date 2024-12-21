from steps.data_ingestion_step import data_ingestion_step
from steps.handle_missing_values_step import handle_missing_values_step

if __name__ == "__main__":
    """
    Entry point for the script.
    """
    print("Starting data ingestion...")
    data_ingestion_step()
    print("Data ingestion completed successfully.")

    print("Starting missing values handling...")
    handle_missing_values_step()
    print("Missing values handling completed.")
