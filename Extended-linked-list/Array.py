class Node:
    def __init__(self, capacity=8):
        self.__data = []
        self.__capacity = capacity
        self.__next = None
        self.__count = 0

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def capacity(self):
        return self.__capacity

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, node):
        self.__next = node

    @property
    def count(self):
        return self.__count
    
    @count.setter
    def count(self, value):
        self.__count = value

    def is_full(self):
        return self.__count == self.__capacity

    def insert(self, value):
        if self.is_full():
            return False

        pos = 0
        while pos < self.__count and self.__data[pos] < value:
            pos = pos + 1

        self.__data.insert(pos, value)
        self.__count = self.__count + 1
        return True

    def remove(self, value):
        try:
            self.__data.remove(value)
            self.__count = self.__count - 1
            return True
        except ValueError:
            return False