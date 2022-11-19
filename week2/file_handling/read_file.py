
with open('text.txt', 'r') as file:
    print(file.read())
    print(file.read(10))

with open('text.txt', 'r') as file:
    print(file.readline())
    print(file.readline(10))

with open('text.txt', 'r') as file:

    # print(file.readlines())

    lines = file.readlines()
    for line in lines:
        print(line)

with open('text.txt', 'r') as file:
    for x in file:
        print(x)