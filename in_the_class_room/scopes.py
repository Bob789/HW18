
def print_y():
    print()

def print_x():
    print_y()
    x = 1
    x += 1
    print('print_x', x)

def print_myx(x: int):
    x = x + 1000
    print('print_myx', x)
x: int = 1
print_x()
print_myx(x)
print('global', x)

def print_list(my_list: list[int]) -> None:
    print('pop', my_list.pop())
    y = 1

def append_list(lst1: list[int]) -> None:
    print('append_list before list()', lst1)
    lst1 = [] # list(). creates new list new address
    #lst1 = lst1.copy()
    lst1.append(100)
    print('append_list', lst1)

def change_list(bbb: list[int]) -> list[int]:
    # global lst1
    aaa = [_**2 for _ in bbb]
    return aaa

lst1: list[int] = [1, 5, 10]
print('global', lst1)
print_list(lst1)
# print_list(lst1.copy())  # save a copy
print('global lst1', lst1)
append_list(lst1)
print('global lst1', lst1)
lst1 = change_list(lst1) # 333
print('after change_list', lst1)
def clear_list(aaa) -> None:
    aaa.clear()  # 999
clear_list(lst1)
print('global after clear', lst1)

def insert_one(dict1: dict) -> None:
    dict1.setdefault('new_key', 10)

def create_new (dict1: dict) -> dict:
    result = {key: value**2 for key, value in dict1.items()}
    return result

dict2 = {'one': 1}
print('before', dict2)
insert_one(dict2)
print('after', dict2)
dict3 = {1: 1, 2: 4, 3: 9}
print(dict3)
dict3 = create_new(dict3)
print(dict3)







