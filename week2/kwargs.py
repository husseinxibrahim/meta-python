
def sum_of(*args):
    sum = 0
    for x in args:
        sum += x
    return sum

print(sum_of(1, 3, 4, 7))

def sum(**kwargs):
    sum = 0
    for x, v in kwargs.items():
        sum += v
    return round(sum, 2)

print(sum(coffee = 8.5, tea = 5))