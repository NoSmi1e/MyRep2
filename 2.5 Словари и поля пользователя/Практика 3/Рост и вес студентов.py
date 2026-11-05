students = {'Сергей': (165, 62), 'Дима': (178, 61), 'Катя': (162, 62), 'Диана': (168, 69)}
print({name: values for name, values in students.items() if values[0] > 167 and values[1] < 75})
