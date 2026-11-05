digits = dict(zip('0123456789', ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')))
print(*(digits[digit] for digit in input()))
