import pandas as pd
import numpy as np

def preprocess_data(data_path):
    """Загружает и предобрабатывает данные для нейросети."""
    df = pd.read_csv(data_path)
    # Пример: нормализация данных
    X = df[['time', 'room', 'teacher']].values
    y = df['schedule_conflict'].values
    return X, y