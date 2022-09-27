
set_a = {1, 2, 3, 4, 5, 5}
set_b = {4, 5, 6, 7, 8, 9}

# sets doesn't accept duplicate values

print(set_a)

set_a.add(8)
print(set_a)

set_a.remove(8)
print(set_a)

set_a.discard(1)
print(set_a)

print(set_a.union(set_b))
print(set_a | set_b)

print(set_a.intersection(set_b))
print(set_a & set_b)

print(set_a.difference(set_b))
print(set_a - set_b)

print(set_a.symmetric_difference(set_b))
print(set_a ^ set_b)

# sets are unordered
print(set_a[0])