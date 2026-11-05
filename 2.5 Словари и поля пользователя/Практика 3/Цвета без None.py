colors = {'b8': 'Grey', 'b9': None, 'a2': 'Green', 'a1': 'Black', 'c10': None, 'a6': 'Pink'}
print({key: value for key, value in colors.items() if value is not None})
