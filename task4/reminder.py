import datetime

def parse_birthday(birthday_str, name):
    try:
        birthday = datetime.datetime.strptime(birthday_str, "%Y.%m.%d").date()
        return birthday
    except ValueError:
        print(f"Error: Invalid date format for {name}. Skipping.")
        return None

def get_upcoming_birthdays(users):
    upcoming_birthdays = []
    today = datetime.date.today()

    for user in users:
        birthday = parse_birthday(user["birthday"], user["name"])
        if birthday is None:
            continue

        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta = birthday_this_year - today
        if 0 <= delta.days <= 7:  # Include birthdays occurring in the next 7 days
            congratulation_date = birthday_this_year
            if congratulation_date.weekday() >= 5:  # If birthday falls on a weekend
                # Move congratulation date to the next Monday
                congratulation_date += datetime.timedelta(days= 7 - congratulation_date.weekday())
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date.strftime("%Y.%m.%d")})

    return upcoming_birthdays
