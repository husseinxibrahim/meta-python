menu = ['Tea', 'Cappuncino', 'Frapacino', 'Juice', 'Catdro', 'Espresso']

def find_coffee(coffee):
    if coffee[0] == 'C':
        return coffee

# map: Applies function to every item in an iterable.
map_coffee = map(find_coffee, menu)

for x in map_coffee:
    print(x)

print('----------------------')
# filter: It returns all elements of an iterable when function returns True.
filter_coffee = filter(find_coffee, menu)

for x in filter_coffee:
    print(x)