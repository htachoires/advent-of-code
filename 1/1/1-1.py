import functools

f = open("../input.txt", "r")
lines = f.readlines()

def only_first_last_digit_to_int(text):
    res = list(filter(str.isdigit, text))
    return int(''.join([res[0], res[-1]]))

digit = functools.reduce(lambda a,b: a+b, [only_first_last_digit_to_int(text) for text in lines])

print("1-1 -> {res}".format(res = digit))