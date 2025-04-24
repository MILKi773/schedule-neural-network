.. _data_preprocessing:

Data Preprocessing Module
=========================

Модуль `data_preprocessing` отвечает за загрузку и предобработку данных для нейросети, используемой в Schedule Neural Network. Он преобразует данные о расписании в формат, подходящий для обучения модели.

.. automodule:: data_preprocessing
    :members:
    :undoc-members:
    :show-inheritance:

Пример использования
--------------------

Ниже приведен пример использования функции `preprocess_data`:

.. code-block:: python

    from data_preprocessing import preprocess_data

    # Загрузка и предобработка данных
    X, y = preprocess_data("data/schedule_data.csv")
    print("Features shape:", X.shape)
    print("Target shape:", y.shape)

Формат входных данных
---------------------

Функция `preprocess_data` ожидает CSV-файл со следующими столбцами:

- `time`: Дата и время занятия (например, "2025-04-24 09:00").
- `room`: Аудитория (например, "A-101").
- `teacher`: ФИО преподавателя.
- `group`: Группа студентов (например, "Group-101").
- `course`: Название курса (например, "Математика").
- `schedule_conflict`: Конфликт в расписании (0 или 1).

.. note::

    Убедитесь, что ваш CSV-файл соответствует этому формату, иначе предобработка завершится с ошибкой.