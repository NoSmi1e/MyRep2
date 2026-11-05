nickname = input()

if (5 <= len(nickname) <= 15
        and nickname.startswith('@')
        and all((ch.isalpha() and ch.islower()) or ('0' <= ch <= '9') for ch in nickname[1:])):
    print('Correct')
else:
    print('Incorrect')
