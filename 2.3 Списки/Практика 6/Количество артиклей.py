words = input().lower().split()
total = sum(word in ('a', 'an', 'the') for word in words)
print(f'Общее количество артиклей: {total}')
