import pytest
import numpy as np
from ml.model import train_model
# TODO: add necessary import

# TODO: implement the first test. Change the function name and input as needed
def null_test():
    # Ensure number of columns in dataset is correct

    data_path = './data/census.csv'
    data = pd.read_csv(data_path)

    expected_cols = 15
    actual_cols = data.shape[1]

    assert actual_cols == expected_cols

# TODO: implement the second test. Change the function name and input as needed
def test_train_model():
    # generate synthetic data for testing
    X_train = np.random.rand(100, 5)
    y_train = np.random.randint(2, size=100)
    
    # training the model
    model = train_model(X_train, y_train)
    
    # check if the model is trained
    assert model is not None
    pass
# TODO: implement the third test. Change the function name and input as needed
def Volume_test():
   
    # Test slice is not empty

    with open('slice_output.txt', 'r') as file:
        content = file.read()

    assert len(content) > 0
