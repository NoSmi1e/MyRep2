balances = {}

def bank(operation, id, amount):
    balances.setdefault(id, 0)
    if operation == 'top up':
        balances[id] += amount
    elif operation in ('withdraw', 'pay'):
        balances[id] -= amount
    elif operation == 'show balance':
        print(balances[id])
