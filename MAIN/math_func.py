import json

def percentage(x=0, y=0):
    return int(x / y * 100)

def add(x, y):
    return x + y

def powerment(x=0, y=0):
    return int(x ** y)


def gen(x=1, y=1, z=1):
    return (x ** 3) + (y ** 3) + (z ** 3) - 3 * (x * y * z)

class Admin:
    def __init__(self):
        self.__data = None

    def connect(self, data_file):
        with open(data_file) as json_file:
            self.__data = json.load(json_file)

    def get_data(self, name):                       # for (Entity e : List)
        for admin in self.__data['admins']:         # if e instance of LE
            if admin['name'] == name:               # return e
                return admin

    def close(self):
        pass

