from itertools import count


def len_tup(t: tuple[int]) -> int:
    return len(t)

def join_tup(tup, tuple99) -> tuple[int]:
    return tup+tuple99

def common_tup(tup, tup8) -> tuple[int]:
    return tuple(i for i in tup if i in tup8)

def diff_tup(tup, tup8) -> tuple[int]:
    return tuple(i for i in tup + tup8 if i not in tup8 or i not in tup)

def el_in_index(tup8, i) -> str:
    return str(tup8[i] if -1 < i < len(tup8) else None)

def reverse_tup(tup8) -> tuple:
    return tup8[::-1]

def mul_tup(tup, mul) -> tuple:
    return tuple(tup for _ in range(mul))

def remove_num(tup8, num) -> tuple[int]:
    return tuple(i for i in tup8 if not i == num)

def no_duplicate(tup8) -> tuple:
    s_list = list(sorted(tup8))
    index: int = 0
    while index < len(s_list):
        while True:
            if s_list.count(s_list[index]) > 1 and index < len(s_list):
                s_list.pop(index)
                index += 1
            else:
                break
        index += 1
    return tuple(s_list)

def find_index_element(tup8, num) -> tuple:
    f_i_e: list[int] = []
    for i in range(len(tup8)):
        if num == tup8[i]:
            f_i_e.append(i)
    return tuple(f_i_e)

def combines_tuple():
    names_list = []
    scores_list = []
    while True:
        name: str = str(input(" Enter name :"))
        if name == "done":
            break
        else:
            names_list.append(name)

    while True:
        score: int = int(input(" Enter score :"))
        if score == -999:
            break
        else:
            scores_list.append(score)

    names: tuple[str] = tuple(names_list)
    scores: tuple[int] = tuple(scores_list)

    return tuple(zip(names, scores))

# solution a
tuple99: tuple[int]  = (99,)
# solution b
tup: tuple[int]      = (77,88,99)
tup8    = (51, 27, 33 , 49, 99, 11, 33, 77 ,85, 27)

print(f" tuple99    : {len_tup(tuple99)}")
# solution c
print(f" tup        : {len_tup(tup)}")
# solution d
print(f" join tuple : {join_tup(tup, tuple99)}")
print(tup)
print(tup8)
# solution e
print(f" common tup  : {common_tup(tup, tup8)}")
# solution f
print(f" diff tup    : {diff_tup(tup, tup8)}")
# solution g
index_t  = int(input(" Enter number index :"))
print(f" print element : {el_in_index(tup8, index_t)}")# element in index (51, 27, 33 , 49, 99, 11, 33, 77 ,85, 27)
# solution h
print(f" print reverse : {reverse_tup(tup8)}")
# solution i
print(f" multiple tuple : {mul_tup(tup, 3)}")
# solution j
print(f" remove num     : {remove_num(tup8, 33)}")# ((51, 27, 33 , 49, 99, 11, 33, 77 ,85, 27)
# solution k
print(f" no duplicate   : {no_duplicate(tup8)}")# (51, 27, 33 , 49, 99, 11, 33, 77 ,85, 27)
# solution l
print(f" find index element: {find_index_element(tup8, 33)}")# (51, 27, 33 , 49, 99, 11, 33, 77 ,85, 27)
#solution m
print(combines_tuple())
#solution 2
# tuple - take less memory performs cose that it faster, restriction the element are constant
# list - Slower, takes more memory, but elements are mutable.

#solution 3
# data_tuple = (
# {"name": "Alice", "age": 30, "city": "New York"}, 1000, "secret-code"
# )
# data_tuple[0] ["age"] = 31
# data_tuple[0] .clear()

# in this case type data_tuple contain 3 index element eich have 3 pointers
# 1 for dict {"name": "Alice", "age": 30, "city": "New York"}
# 2 value int 1000
# 3 value str "secret-code"
#
#     the first pointer point on dict, it is not meter what contain dict inside the pointer not change.
#     the rest object can't change there have no attribute to change they const read only.







