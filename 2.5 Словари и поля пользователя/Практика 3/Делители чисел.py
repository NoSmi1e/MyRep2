numbers = [24, 5, 17, 9, 28, 84, 62]
print({number: [divisor for divisor in range(1, number + 1) if number % divisor == 0] for number in numbers})
