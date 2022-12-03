#calculator

#add
def add(n1 , n2):
 return n1 + n2
#subtract
def subtract( n1 , n2):
 return n1 - n2
#mutiply
def multiply(n1 , n2):
 return n1 * n2

def divide(n1 , n2):
 return n1 / n2

operations = {
 '+': add,
 '-': subtract,
 '*': multiply,
 '/': divide,
#operation

}

num1 = int(input('enter the first number:\n'))

num2 = int(input('enter the second:\n'))


for symbols in operations:
 print(symbols)

 operations_symbols = input('enter the symbol you would like to type:\n')

cal_fuction = operations[operations_symbols]
answer = cal_fuction(num1, num2)

print(f'{num1}{operations_symbols} {num2} = {answer}')
