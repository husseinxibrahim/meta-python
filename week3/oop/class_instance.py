
from typing_extensions import Self


class Myclass():
    a = 5
    pass

myc = Myclass()
print(Myclass.a)
print(myc.a)

class Myclass2():
    def Hello(self):
        print("Hello world")
    pass

myc2 = Myclass2()
myc2.Hello()
Myclass2.Hello()