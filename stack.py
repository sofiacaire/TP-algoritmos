class Stack:
    def __init__(self):
        self.__elements = []

    def push(self, value):
        self.__elements.append(value)

    def pop(self):
        return self.__elements.pop()

    def size(self):
        return len(self.__elements)

    def show(self):
        print(self.__elements)
