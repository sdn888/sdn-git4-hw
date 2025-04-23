import pandas as pd
import numpy as np


# Функция для проверки, является ли дата праздничным днем
def is_holiday(date):
    # Список праздничных дней (пример на 2023 год)
    holidays = pd.to_datetime([
        '2023-01-01', '2023-01-02', '2023-01-07',  # Новый год и Рождество
        '2023-02-23', '2023-03-08',  # Защитник Отечества, Международный женский день
        '2023-05-01', '2023-05-09',  # Праздник Весны и Труда, День Победы
        '2023-06-12',  # День России
        '2023-11-04',  # День народного единства
        # Добавьте другие праздничные дни по необходимости
    ])
    return date in holidays


# Функция для вычисления календарных и рабочих дней
def calculate_days(start_date, end_date):
    # Генерируем диапазон дат
    dates = pd.date_range(start=start_date, end=end_date)

    # Количество календарных дней
    total_days = len(dates)

    # Количество рабочих дней (без выходных и праздничных)
    # Рабочие дни: с понедельника по пятницу
    weekdays = dates[dates.weekday < 5]  # Понедельник=0, Воскресенье=6
    working_days = [d for d in weekdays if not is_holiday(d)]

    return total_days, len(working_days)


# Пример использования
if __name__ == "__main__":
    start_date_input = input("Введите начальную дату (DD-MM-YYYY): ")
    end_date_input = input("Введите конечную дату (DD-MM-YYYY): ")

    # Преобразуем даты из формата DD-MM-YYYY в формат YYYY-MM-DD
    start_date = pd.to_datetime(start_date_input, format='%d-%m-%Y')
    end_date = pd.to_datetime(end_date_input, format='%d-%m-%Y')

    total_days, working_days = calculate_days(start_date, end_date)

    print(f"Количество календарных дней: {total_days}")
    print(f"Количество рабочих дней: {working_days}")