my_list = [1, 2, 3]

#Traditional Function
def add_list(list, item):
    list.append(item)
    return list

#pure function is a function that does not change or have any effect on a variable, data, list, or sets beyond its own scope.
def add_to_list(list, item):
    new_list = list.copy()
    new_list.append(item)
    return new_list

#Pure
func1 = add_to_list(my_list, 4)
#Traditional
func2 = add_list(my_list, 4)

print(func1)
print(func2)