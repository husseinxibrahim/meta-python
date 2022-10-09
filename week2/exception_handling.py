def divide(a, b):
    return a / b

print(divide(40, 4))

try:
    print(divide(40, 0))

except Exception as e:
    print("something went wrong", e)
    print(e.__class__)
except ZeroDivisionError as e:
    print("Wrong division")