import re

def normalize_phone(phone_number):
    # remove all excepr digits and '+'
    normalized_number = re.sub(r'\D', '', phone_number)

    # add '+38' if needed
    if not normalized_number.startswith('+'):
        if normalized_number.startswith('380'):
            normalized_number = '+' + normalized_number
        else:
            normalized_number = '+38' + normalized_number

    return normalized_number
