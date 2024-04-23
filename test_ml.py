import pytest
import numpy as np
import pandas as pd
from ml.model import train_model
# TODO: add necessary import
#set up for testing
#test 1
#
@pytest.fixture
def null_data():   
    data_path = './data/census.csv'
    data = pd.read_csv(data_path)
    actual_cols = data.shape[1]
    return actual_cols
#test 2
@pytest.fixture
def model_test():
# generate synthetic data for testing
    X_train = np.random.rand(100, 5)
    y_train = np.random.randint(2, size=100)
# training the model
    model = train_model(X_train, y_train)
    return model

#test 3
@pytest.fixture
#read file into a DF
def content():
    with open('slice_output.txt', 'r') as file:
        content = file.read()
    return content

# TODO: implement the first test. Change the function name and input as needed
def test_columns(null_data):
    expected_cols = 15
    # Ensure number of columns in dataset is correct 
    assert null_data == expected_cols


# TODO: implement the second test. Change the function name and input as needed
def test_train_model(model_test):    
    # check if the model is trained
    assert model_test is not None


# TODO: implement the third test. Change the function name and input as needed
# Test slice is not empty
def test_volumne(content):
    assert len(content) > 0
