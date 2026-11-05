text = input().lower()
words = [word.translate(str.maketrans('', '', '.,;:-?!')) for word in text.split()]
print(len({word for word in words if word}))
