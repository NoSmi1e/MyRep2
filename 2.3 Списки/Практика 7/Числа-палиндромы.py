palindromes = [number for number in range(100, 1001) if str(number) == str(number)[::-1]]
print(palindromes)
