import re

def is_palindrome(s):
    s = str(s)
    s = s.lower()
    mystr = re.sub(r"[\W_]*", "", s)
    reverse = mystr[::-1]
    return mystr == reverse