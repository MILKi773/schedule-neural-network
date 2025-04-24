import pytest
from src.model import create_model

def test_create_model():
    model = create_model(input_shape=(10, 3))
    assert model is not None
assert len(model.layers) == 4