calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string_):
    Length = len(string_)
    Result = (Length, string_.upper(), string_.lower())
    count_calls()
    return Result
def is_contains(str_, list_):
    Contain = False
    for i in range(len(list_)):
        if str_.lower() == list_[i].lower():  # сравниваем значения, преобразованные в строчные символы
            Contain = True
    count_calls()
    return Contain

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
