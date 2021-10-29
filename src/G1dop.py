from dotenv import dotenv_values
config = dotenv_values('.env')
string_empty = config['empty']
empty = int(string_empty)

def get_square(empty):
    result = (('*' * empty) + '\n') * empty
    for i in range(empty):
        return(result)
square1 = get_square(empty)
print(square1)

try:
    empty = int(string_empty)
except ValueError:
    raise ValueError(f'Не могу превратить значение {string_empty} в число')
if empty <= 0:
    raise ValueError('Сторона квадрата должна быть больше нуля')

square1 = get_square(empty)
