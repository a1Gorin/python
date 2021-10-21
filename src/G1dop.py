from dotenv import dotenv_values
config = dotenv_values('.env')
string_empty = config['empty']
empty = int(string_empty)

def get_square(empty):
    for i in range(empty):
        print('*' * empty)
square1 = get_square(empty)
print(square1)