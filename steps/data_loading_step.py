import pandas as pd
import zenml.steps as step

@step
def load_data():
    train_data = pd.read_csv('./data/transformed/transformed_combined_train.csv')
    test_data = pd.read_csv('./data/transformed/tranformed_combined_test.csv')

    return train_data, test_data