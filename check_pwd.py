# CS362
# A2: TDD Hands On
# by Kongkom Hiranpradit ONID ID: hiranprk
# 12 November 2023

def check_pwd(pwd):
    """ test strings """
    lower = "abcdefghijklmnopqrstuvwxyz"

    """ rule 1: Must be between 8 and 20 characters (inclusive) """
    if len(pwd) < 8 or len(pwd) > 20:
        return False

    """ rule 2: Must contain at least one lowercase letter (standard English alphabet) """
    lowercase_n = 0
    for i in pwd:
        if i in lower:
            lowercase_n += 1

    if lowercase_n <= 0:
        return False

    else:
        return True
