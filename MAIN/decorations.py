
def decoration_operation(func):
    def wrapper_func(u, v):
        if v == 0:
            return
        return u / v
    return wrapper_func


@decoration_operation
def operation(x, y):
    return x / y


print("oper:", operation(1,1))


# Operator Overloading
class Square:

    def __init__(self, side):
        self.__side = side

    def setSide(self, side):
        self.__side = side

    def getSide(self):
        return self.__side

    def Perimeter(self):
        return self.__side * 4

    def Area(self):
        return self.__side ** 2

    def __add__(self, other):
        return Square(self.__side + other.__side)


Square1 = Square(2)
Square2 = Square(4)
Square3 = Square1 + Square2


def func():
    x = 5  # local var

    def nested():
        global x
        y = 0
        x = 100 + y

    # print("1 - ", x)
    nested()
    # print("2 - ", x)


x = 20
# print("3 - ", x)
func()
# print("4 - ", x)


def myDecorator(func):
    print("Decorator Initalised...")
    func()


@myDecorator
def myFunc():
    print("MyFunc")

