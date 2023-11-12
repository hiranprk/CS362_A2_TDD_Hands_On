# CS362
# A2: TDD Hands On
# by Kongkom Hiranpradit ONID ID: hiranprk
# 12 November 2023

def check_pwd(pwd):
    """ test strings """
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digit = "0123456789"

    """ rule 1: Must be between 8 and 20 characters (inclusive) """
    if len(pwd) < 8 or len(pwd) > 20:
        return False

    lowercase_n = 0
    uppercase_n = 0
    digit_n = 0
    for i in pwd:
        if i in lower:
            lowercase_n += 1
        elif i in upper:
            uppercase_n += 1
        elif i in digit:
            digit_n += 1

    """ rule 2: Must contain at least one lowercase letter (standard English alphabet) """
    if lowercase_n <= 0:
        return False

    """ rule 3: Must contain at least one uppercase letter (standard English alphabet) """
    if uppercase_n <= 0:
        return False

    """ Rule 4: Must contain at least one digit """
    if digit_n <= 0:
        return False

    else:
        return True
