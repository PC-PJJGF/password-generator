import re
import random
import string

PASSWORDREGEX = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"

def validate_passwd(passwd):
    return re.match(PASSWORDREGEX, passwd) is not None

def generate_passwd(passwd_length):    
    lowerCase = string.ascii_lowercase
    upperCase = string.ascii_uppercase
    digits = string.digits
    special = "@$!%*?&"
    
    password = [
        random.choice(lowerCase),
        random.choice(upperCase),
        random.choice(digits),
        random.choice(special)
    ]
    
    all_characters = lowerCase + upperCase + digits + special
    password += random.choices(all_characters, k=passwd_length - 4)
    
    random.shuffle(password)
    
    passwd_str = ''.join(password)
    
    if validate_passwd(passwd_str):
        return passwd_str
    else:
        return generate_passwd(passwd_length)