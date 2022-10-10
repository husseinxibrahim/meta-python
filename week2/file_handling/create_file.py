
with open('new.txt', 'w')as file:
    file.writelines(["This is a new file\n", "This is a second line\n"])


with open('new.txt', 'a')as file:
    file.writelines(["This is a new file\n", "This is a second line\n"])


try:
    with open('path/new2.txt', 'w')as file:
        file.writelines(["This is a new file\n", "This is a second line\n"])
except FileNotFoundError as e:
    print('Error!', e)