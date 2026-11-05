phones = {}
for _ in range(int(input())):
    phone, name = input().split()
    phones.setdefault(name.lower(), []).append(phone)
for _ in range(int(input())):
    print(' '.join(phones.get(input().lower(), ['абонент не найден'])))
