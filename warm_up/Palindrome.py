"Check whether a number reads the same backward."

def isPalindrome(x):
    if x < 0:
        return False
    return str(x) == str(x)[::-1]
