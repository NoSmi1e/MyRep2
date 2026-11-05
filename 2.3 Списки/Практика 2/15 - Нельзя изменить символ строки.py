# При запуске возникает TypeError: 'str' object does not support item assignment.
s = '31415'
s[0] = '10'
s[4] = '3'
s[-1] = '9'
print(s)
