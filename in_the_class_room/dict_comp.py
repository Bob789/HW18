
# not recommended
# power_3: dict[int: int] = {
#     1: 3,
#     2: 8,
#     3: 27
# }

power_3: dict[int: int] = dict()
for i in range(1, 10 + 1):
    power_3[i] = i ** 3
print(power_3)

print([ x**3 for x in range(1, 10 + 1) ])

print({x**3 : x for x in range(1, 10 + 1)})

id_name = {10: 'danny', 20: 'moshe', 30: 'jim', 100: 'yakir'}
print(id_name)
new_id_name = dict()
for key, value in id_name.items():
    new_id_name[key] = value.upper()
print(new_id_name)

new_id_name = {key: value.upper() for key, value in id_name.items()}
print(new_id_name)
print(new_id_name := {key: value.upper() for key, value in id_name.items()})

