# Создаём переменную Calls = 0 вне функций
calls = 0

# Создаём функцию count_calls и изменим в ней значение переменной Calls.
def count_calls():
    global calls
    calls += 1

# Создаём функцию string_info с параметром string и реализуем логику работы по описанию
def string_info(s):
    count_calls()
    return (len(s), s.upper(), s.lower())

# Создаём функцию is_contains с двумя параметрами string и list_to_search, реализуем логику работы по описанию
def is_contains(string, list_to_search):
    count_calls()
    string_lower = string.lower()
    list_to_search_lower = [item.lower() for item in list_to_search]
    return string_lower in list_to_search_lower

# Вызываем соответствующие функции string_info и is_contains произвольное количество раз с произвольными данными.
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) 
print(is_contains('cycle', ['recycling', 'cyclic']))  

# Отображаем значения переменной вызовов на экране (на консоли)
print(calls)
