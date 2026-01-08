"Reverse digits of an integer."

def reverse(x):
    sign = -1 if x < 0 else 1
    x = abs(x)
    rev = int(str(x)[::-1])
    return sign * rev
