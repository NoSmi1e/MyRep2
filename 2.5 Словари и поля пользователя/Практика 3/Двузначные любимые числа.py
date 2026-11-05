favorite_numbers = {'scarlett': 41, 'den': 22, 'viktor': 321, 'lera': 777, 'mahad': 4, 'manny': 4, 'ken': 8423, 'borya': 12}
print({name: number for name, number in favorite_numbers.items() if 10 <= abs(number) <= 99})
