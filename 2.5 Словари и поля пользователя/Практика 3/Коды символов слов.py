words = ['кошка', 'собака', 'мышь']
print({word: [ord(char) for char in word] for word in words})
