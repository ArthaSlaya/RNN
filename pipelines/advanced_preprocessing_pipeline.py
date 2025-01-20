from zenml.pipelines import pipeline
from steps.advanced_preprocessing_step import advanced_preprocessing_step

@pipeline(enable_cache= False)
def advanced_preprocessing_pipeline():
    """
    Defines the advanced preprocessing pipeline.
    It consists of:
    1. Loading processed data.
    2. Applying advanced preprocessing methods.
    3. Saving the transformed data.
    """
    advanced_preprocessing_step()