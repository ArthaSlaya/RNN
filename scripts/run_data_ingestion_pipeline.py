from pipelines.data_ingestion_pipeline import data_ingestion_pipeline
from steps.data_ingestion_step import data_ingestion_step

def run_data_ingestion_pipeline() -> None:
    """
    Runs the data ingestion pipeline.
    """
    pipeline = data_ingestion_pipeline(data_ingestion= data_ingestion_step())
    pipeline.run()