from pipelines.vectorization_pipeline import vectorization_pipeline
from steps.vectorization_step import vectorization_step

def run_vectorization_pipeline() -> None:
    """
    Runs the text vectorization pipeline.
    
    This script:
    - Initializes the ZenML vectorization pipeline.
    - Executes the pipeline to vectorize the processed datasets.
    - Saves the vectorized output in the `./data/vectorized` directory.
    """
    # Instantiate and run the vectorization pipeline
    vectorization_pipeline()
    