number = input()
allowed_letters = 'АВЕКМНОРСТУХ'

if (len(number) in (9, 10)
        and number[0] in allowed_letters
        and all('0' <= ch <= '9' for ch in number[1:4])
        and all(ch in allowed_letters for ch in number[4:6])
        and number[6] == '_'
        and all('0' <= ch <= '9' for ch in number[7:])):
    print('YES')
else:
    print('NO')
