from zenml.pipelines import pipeline
from steps.data_ingestion_step import data_ingestion_step

@pipeline(enable_cache=False)
def data_ingestion_pipeline():
    """
    Pipeline: Runs the data ingestion step.

    Parameters:
    - data_ingestion (callable): A callable ZenML step for data ingestion.
    """
    # Instantiate the pipeline
    data_ingestion_step()