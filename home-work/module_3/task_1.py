# Перше завдання
# Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.

# Вимоги до завдання:
# Функція приймає один параметр: date — рядок, що представляє дату у форматі 'РРРР-ММ-ДД' (наприклад, '2020-10-09').
# Функція повертає ціле число, яке вказує на кількість днів від заданої дати до поточної. Якщо задана дата пізніша за поточну, результат має бути від'ємним.
# У розрахунках необхідно враховувати лише дні, ігноруючи час (години, хвилини, секунди).
# Для роботи з датами слід використовувати модуль datetime Python.


# Рекомендації для виконання:
# Імпортуйте модуль datetime.
# Перетворіть рядок дати у форматі 'РРРР-ММ-ДД' у об'єкт datetime.
# Отримайте поточну дату, використовуючи datetime.today().
# Розрахуйте різницю між поточною датою та заданою датою.
# Поверніть різницю у днях як ціле число.


# Критерії оцінювання:
# Коректність роботи функції: функція повинна точно обраховувати кількість днів між датами.
# Обробка винятків: функція має впоратися з неправильним форматом вхідних даних.
# Читабельність коду: код повинен бути чистим і добре документованим.

# =========================================================================================================

from datetime import datetime

def get_days_from_today(date: str = None):
    if date is None:
        return datetime.now().day
    
    try:
        input_date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        return 0
    
    date_now = datetime.now()

    return (input_date - date_now).days


result_next_year = get_days_from_today('2027-10-09')
result_current_year = get_days_from_today('2026-01-01')
result_wrong_arg_str = get_days_from_today('2222-')
result_forgot_arg = get_days_from_today()

print(f"Next year pls: {result_next_year}")
print(f"Current year pls: {result_current_year}")
print(f"Ups, wrong arg: {result_wrong_arg_str}")
print(f"Ups, forgot arg, pls return current day: {result_forgot_arg}")
    
