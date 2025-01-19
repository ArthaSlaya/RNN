from zenml.pipelines import pipeline
from steps.preprocessing_step import preprocessing_step

@pipeline(enable_cache= False)
def preprocessing_pipeline():
    """
    Pipeline: Runs the preprocessing step.
    """
    preprocessing_step()