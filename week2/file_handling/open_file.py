
file = open('text.txt', mode='r')

data = file.readlines()

print(data)

file.close()

#This method close file automatically
with open('text.txt', mode='r') as file:
    data = file.readlines()

    print("\n", data)