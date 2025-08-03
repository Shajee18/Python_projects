import random
import string

all_chrs = string.ascii_letters + string.digits + string.punctuation


def is_strong(password):
    return (
        len(password)>=8 and
        any(c.islower() for c in password )and
        any(c.isupper() for c in password)and
        any(c.isdigit()for c in password)and
        any(c in string.punctuation for c in password )
    )
user_pass = input("enter a passwoord:" )
if is_strong(user_pass):
    print("your password is strong:" , user_pass )
else:
    strong_pass = ''.join(random.choices(all_chrs , k = 12))
    print("its to weak.\nhere is a strong one:" , strong_pass )