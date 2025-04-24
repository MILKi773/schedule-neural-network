import tensorflow as tf
from data_preprocessing import preprocess_data
from model import create_model

def train_model(data_path, model_path):
    """Обучает модель и сохраняет ее."""
    X, y = preprocess_data(data_path)
    model = create_model(input_shape=(X.shape[1], X.shape[2]))
    model.fit(X, y, epochs=10, batch_size=32, validation_split=0.2)
    model.save(model_path)

if __name__ == "__main__":
    train_model("data/schedule_data.csv", "models/schedule_model.h5")