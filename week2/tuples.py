my_tuple = (5, "strings", True)

print(my_tuple[1])

print(my_tuple.count('strings'))

print(my_tuple.index(True))

for x in my_tuple:
    print(x)

# Tuples are immutable
my_tuple[0] = 3
