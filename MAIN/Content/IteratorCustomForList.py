class IteratorCustomForList:
    def __init__(self, listIN):
        self.__list = listIN
        self.__index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.__index += 1
        if self.__index == len(self.__list):
            raise Exception
        return self.__list[self.__index]