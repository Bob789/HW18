import statistics

tup1: tuple[int, int, int, int] = (1, 3, 5, 10)
tup2: tuple[int, int, int, str] = (1, 3, 5, 'hello')
tup3: tuple[int] = (1,)
tup4: tuple[int, int, int, int] = (1, 3, 5, 10)
print(tup4[0])
#                                            1,     2, 3,  4
tup5: tuple[list[int], int, int, int] = ([1, 2, 3], 3, 5, 10)
print(tup5)
tup5[0].clear()
print(tup5)

fix_prices: tuple = ([1, 2, 3], 3, 5, 10)
prices: list[any] = [[1, 2, 3], 3, 5, 10]
prices[0] =           'hello'
prices.append(2)
prices.remove(3)

# [x for x in range(10)] -- list
# {x:x**2 for x in range(10)} -- dict
# tuple(x for x in range(10)) -- tuple
print(tuple(x for x in range(10)))

israel = {'name': 'israel', 'birth': 1948, 'pop': 9.0}
japan = {'name': 'japan', 'birth': 1719, 'pop': 120}
countries: tuple[any, any] = (israel, japan)
israel['pop'] += 1
print(countries[0])

tup6 = ((1, {'name': 'shani'}), 3, 4)
print(tup6[0][1]['name'])

fruits: tuple[str, str, str] = ("apple", "banana", "cherry")  # immutable
print(fruits)
print(fruits[0])
list_tup = list({'name': 'israel', 'birth': 1948, 'pop': 9.0}.items())
print(list_tup)
list_tup.remove(('pop', 9.0))
print(list_tup)

create_nested_tuple: tuple[tuple[any]] = (
    ("Alice", 21, "Physics"),
    ("Bob", 222, "Chemistry"),
    ("Charlie", 20, "Mathematics")
)
print(create_nested_tuple)

apple = 1
fruits2: tuple[int, str, str] = (apple, "banana", "cherry")  # immutable
print(fruits2)
apple = 2
print(fruits2)

apple2 = "apple"
fruits2: tuple[str, str, str] = (apple2, "banana", "cherry")  # immutable
apple2 += "!"
print(fruits2)

print('-----------------------')
numbers: tuple[int, int, int, int, int, int, int] = (1, 2, 0, 3, 2, 100, 2)
print(numbers.count(2))  # 3
print(numbers.index(100))  # 5
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(statistics.mean(numbers))
print(sum(numbers))
print(any(numbers))
print(all(numbers))
sorted_tuple = tuple(sorted(numbers))
# numbers.sort -- no

print(sorted_tuple)
print('--')
tuple_1 : tuple[int, int] = (1, 2)
tuple_2 : tuple[int, int] = (3, 4)
print(tuple_1 + tuple_2)
print(tuple_1 * 3)
print(3 in tuple_2)
print(tuple(x * 3 for x in tuple_1 + tuple_2))
l1 = []
for x in range(1, 4 + 1):
    l1.append(x ** 3)
print(list(tuple(l1)))

grades = (("Alice", 92), ("Bob", 90), ("Charlie", 88), ("David", 85), ("Eve", 79))
# create a new tuple of these pairs sorted by grades
print(tuple(sorted(grades, key=lambda pair: pair[1])))

names: tuple[str] = ("Alice", "Bob", "Charlie")
scores: tuple[int] = (80, 90, 99, 100)
combines_tuple: tuple[tuple[any]] = tuple(zip(names, scores))
print(combines_tuple)
list_combined = list(zip(names, scores))
print(list_combined)
print(dict(zip(names, scores)))

keys = ['name', 'age', 'city']
values = ['Alice', 25, 'New York']
result = {keys[i]: values[i] for i in range(min(len(keys), len(values)))}
print(result)