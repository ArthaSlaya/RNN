from zenml.pipelines import pipeline
from steps.vectorization_step import vectorization_step

@pipeline(enable_cache= False)
def vectorization_pipeline():
    """
    ZenML pipeline to execute the text vectorization step.
    This pipeline runs the vectorization_step that:
    - Loads processed training and test data.
    - Applies Word2Vec vectorization.
    - Saves the vectorized datasets.
    """
    vectorization_step()