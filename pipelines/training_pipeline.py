from zenml.pipelines import pipeline

@pipeline(enable_cache= False)
def training_pipeline(load_data_step, training_model_step, evaluate_model_step):
    """
    Training pipeline for data processing and model training.

    This pipeline performs the following steps:
    1. Loads the preprocessed training and test data.
    2. Trains an RNN, LSTM, GRU models using the training data.
    3. Evaluates the models on the test data.

    Args:
        load_data_step: A step that loads the transformed datasets.
        training_step: A step that trains and evaluates the model.
    """
    train_data, test_data = load_data_step()
    model, history = training_model_step(train_data, test_data)
    evaluate_model_step(model, test_data, history)