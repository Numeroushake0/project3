from datetime import datetime, date

def get_days_from_today(date_str):
    try:
        input_date = datetime.strptime(date_str, '%Y-%m-%d').date()  
        today = date.today()  

        delta = input_date - today
        return delta.days

    except ValueError:
        return "Невірний формат дати. Будь ласка, використовуйте формат 'РРРР-ММ-ДД'"

print(get_days_from_today("2023-01-31")) 