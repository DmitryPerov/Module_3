def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)

print_params(a = 2.7, b = 'Питон') # вызов функции с разными аргументами
print_params(c = 'Питон', a = 2.7) # вызов функции с разными аргументам в измененном порядке
print_params()                     # вызов функции без аргументов

print_params(b = 25)                # проверка с заданными параметрами
print_params(c = [1,2,3])           # проверка с заданными параметрами

values_list = [[2,6,5], True, 'Иван']
values_dict = {"a": 7, "b": 'Петр', "c": True}
print_params(*values_list)        # распаковка параметров (для списка)
print_params(**values_dict)       # распаковка параметров (для словаря)

values_list_2 = [54.32, 'Строка' ]   # распаковка с отдельными параметрами
print_params(*values_list_2, 42)