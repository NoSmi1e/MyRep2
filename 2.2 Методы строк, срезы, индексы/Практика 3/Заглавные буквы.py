first_name, last_name = input().split()

if first_name[0].isupper() and last_name[0].isupper():
    print('YES')
else:
    print('NO')
