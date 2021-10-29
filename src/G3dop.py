from dotenv import dotenv_values
config = dotenv_values('.env')
string_zero = config['zero']
zero = 0

def fivehundred(zero):
    for i in range(zero, 501):
        zero = zero + i
    return(zero)
rez1 = fivehundred(zero)
print(rez1)