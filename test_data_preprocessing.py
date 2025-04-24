import pytest
from src.data_preprocessing import preprocess_data

def test_preprocess_data():
    X, y = preprocess_data("data/schedule_data.csv")
    assert X is not None
    assert y is not None