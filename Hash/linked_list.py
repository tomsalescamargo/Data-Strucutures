class Element:
    def __init__(self, key, value):
        self.__key = key
        self.__value = value
        self.__next = None

    def get_value(self):
        return self.__value

    def get_key(self):
        return self.__value

    def get_next(self):
        return self.__next

    def set_next(self, next_element):
        self.__next = next_element


class LinkedList:

    def __init__(self):
        self.__first = None
        self.__last = None

    def add_last(self, key, value):
        new_element = Element(key, value)

        if self.__first == None:
            self.__first = new_element
            self.__last = new_element
        else:
            self.__last.set_next(new_element)
            self.__last = new_element

    def remove_last(self):

        if self.__first == None:
            return False

        if self.__first == self.__last:
            self.__first = None
            self.__last = None
        else:
            iterator = self.__first
            while iterator.get_next() != self.__last:
                iterator = iterator.get_next()

            iterator.set_next(None)
            self.__last = iterator

    def search(self, key):
            iterator = self.__first
            while iterator != None and iterator.get_key() != key:
                iterator = iterator.get_next()

            return iterator