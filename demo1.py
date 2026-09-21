def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return not is_even(n)

def absolute_value(x):
    if x < 0:
        print('this value is negative')
        return -x
    return x

print(absolute_value(-23))
