from datetime import datetime

def get_days_from_today(date):
    """Function return difference between current date and input date"""
    try:
        date_obj = datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        return "Wrong date format. Expected format is 'yyyy-mm-dd'"  

    today = datetime.today()
    delta = today - date_obj

    return delta.days
