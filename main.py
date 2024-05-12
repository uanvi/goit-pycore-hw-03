from task1.date_calc import get_days_from_today
from task2.lottery_calc import get_numbers_ticket
from task3.normalize import normalize_phone
from task4.reminder import get_upcoming_birthdays

print (get_days_from_today("20241-05-06"))

print("Random numbers:", get_numbers_ticket(1, 1000, 100))


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Normalized phone numbers for SMS:", sanitized_numbers)


# Example usage
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Invalid User", "birthday": "1990"},  # Invalid date format
    {"name": "Mr Anderson", "birthday": "1976.05.14"},
    {"name": "Mr Anderson", "birthday": "2000.02.28"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
