from dotenv import dotenv_values
config = dotenv_values('.env')
string_a = config['a']
string_b = config['b']
a = int(string_a)
b = int(string_b)

def get_rectangle(a,b):
    print(a * b)
square2 = get_rectangle(a,b)
print(square2)