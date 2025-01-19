from pipelines.preprocessing_pipeline import preprocessing_pipeline
from steps.preprocessing_step import preprocessing_step

def run_preprocessing_pipeline() -> None:
    """
    Runs the preprocessing pipeline.
    """
    # Instantiate and run the pipeline
    preprocessing_pipeline()