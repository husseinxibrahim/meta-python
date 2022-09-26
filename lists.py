
list = [1, 2, 3, 4, 5]
print(list)
print(*list , sep=", ")

list.insert(len(list), 6)
print(list)

list.append(7)
print(list)

list.extend([8, 9, 10])
print(list)

list.pop(2)
print(list)

del list[1]
print(list)

for x in list:
    print('Value: ', x)