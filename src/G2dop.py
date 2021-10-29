from dotenv import dotenv_values
config = dotenv_values('.env')
string_a = config['a']
string_b = config['b']
a = int(string_a)
b = int(string_b)

def get_rectangle(a,b):
    final = a * b
    return (final)
square2 = get_rectangle(a,b)
print(square2)

try:
    a = int(string_a)
    b = int(string_b)
except ValueError:
    raise ValueError(f'Не могу превратить значение {string_a} в число')
    raise ValueError(f'Не могу превратить значение {string_b} в число')
if a and b <= 0:
    raise ValueError('Длина и ширина прямоугольника должны быть больше нуля')

square = get_rectangle(a,b)

print(f'Площадь прямоугольника длиной {a} и шириной {b} равна {square2}')