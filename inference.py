from tensorflow.keras.models import load_model
from data_preprocessing import preprocess_data

def predict_schedule(data_path, model_path):
    """Предсказывает расписание с помощью обученной модели."""
    X, _ = preprocess_data(data_path)
    model = load_model(model_path)
    predictions = model.predict(X)
    return predictions