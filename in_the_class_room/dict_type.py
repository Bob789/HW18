
# info: dict[str, any] = {'id': 1, 'name': 'jimmy', 'age': 29}
# info['age'] = 30
# info['age'] += 1
# new_age = int(input('enter your age:'))
# info['age'] = new_age
#
# info['age'] = int(input('enter your age:'))

def add(a: float, b: float) -> float:
    return a + b
def minus(a: float, b: float) -> float:
    return a - b
def mul(a: float, b: float) -> float:
    return a * b
def div(a: float, b: float) -> float:
    return a / b

x = 3
y = 4
print(add(x, y))

dic_op = {'+': add, '-': minus, '*': mul, '/': div}  # def(x,y) -> z
print(add        (x, y))
print(dic_op['+'](x,y))
x = float(input('enter x:'))
user_op = ''
while not user_op in ['+', '-', '*', '/']:
    user_op = input('operation [+ - * /]')
y = float(input('enter x:'))
#result = add(x, y)
result = dic_op[user_op](x, y)
print(f"{x} {user_op} {y} = {result}")

def option_1():
    print('doing option 1')

menu_op = { "1": option_1}
user_choice = input("what's your choice?")
menu_op[user_choice]()

def add(a: float, b: float) -> float:
    return a + b

#lambda a, b: a + b

x = float(input('enter x:'))
user_choice = ''
while not user_choice in ['+', '-', '*', '/']:
    usr_choice = input('operation [+ - * /]')
y = float(input('enter x:'))


dic_op1 = {'+': add, '-': minus, '*': mul, '/': div}  # def(x,y) -> z
dic_op2 = {'+': lambda a, b: a + b, '-': minus, '*': mul, '/': div}  # def(x,y) -> z

print(add        (x, y))
print(dic_op[user_choice](x, y))

# if user_choice == '+':
#     add(x, y)

# match user_choice:
#     case '+': add(x, y)






