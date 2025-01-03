from zenml.pipelines import pipeline

@pipeline
def data_ingestion_pipeline(data_ingestion: callable) -> None:
    """
    Pipeline: Runs the data ingestion step.

    Parameters:
    - data_ingestion (callable): A callable ZenML step for data ingestion.
    """
    data_ingestion()