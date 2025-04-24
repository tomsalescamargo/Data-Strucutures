from linked_list import LinkedList


class Hash:

    def __init__(self, table_length):
        self.__array = []
        self.__table_length = table_length

    def search(self, key):
        bucket = key % self.__table_length
        if not isinstance(self.__array[bucket], LinkedList):
            return False

        self.__array[bucket].search(key)

    def include(self, key, value):
        bucket = key % self.__table_length
        if not isinstance(self.__array[bucket], LinkedList):
            self.__array[bucket] = LinkedList()

        self.__array[bucket].add_last(key, value)

    def remove(self, key):
        bucket = key % self.__table_length
        if not isinstance(self.__array[bucket], LinkedList):
            return False

        self.__array[bucket].remove_last(key)


hash_table = Hash(5)

# Incluindo dados
hash_table.include(10, "Valor 10")  # 10 % 5 == bucket 0
hash_table.include(12, "Valor 12")  # 12 % 5 == bucket 2
hash_table.include(15, "Valor 15")  # 15 % 5 == bucket 0

# Pesquisando dados
hash_table.search(10)
hash_table.search(12)

# Removendo dados
hash_table.remove(15)