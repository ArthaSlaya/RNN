import logging
from pipelines.advanced_preprocessing_pipeline import advanced_preprocessing_pipeline
from steps.advanced_preprocessing_step import advanced_preprocessing_step

# Set up logging
logging.basicConfig(level= logging.INFO, format= "%(asctime)s - %(levelname)s - %(message)s")

def run_advanced_preprocessing_pipeline():
    """
    Orchestrates and runs the advanced preprocessing pipeline.
    """
    logging.info("Initializing the advanced preprocessing pipeline...")

    # Instantiate the pipeline
    pipeline_instance = advanced_preprocessing_pipeline(
        advanced_preprocessing_step= advanced_preprocessing_step()
    )

    # Run the pipeline
    logging.info("Running the advanced preprocessing pipeline...")
    pipeline_instance.run()

    logging.info("Advanced preprocessing pipeline completed successfully.")