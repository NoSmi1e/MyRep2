s = '3:animal 4:house 8:tree 2:color 21:moon 31:fire 12:ship'
print({int(key): value for key, value in (pair.split(':') for pair in s.split())})
