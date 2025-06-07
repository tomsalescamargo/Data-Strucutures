from Array import Node

class ExtendedLinkedList:
    def __init__(self, node_capacity=8):
        self.__head = None
        self.__node_capacity = node_capacity

    def split_node(self, node_to_split):
        new_node = Node(self.__node_capacity)

        mid_point = node_to_split.capacity // 2

        new_node.data = node_to_split.data[mid_point:]
        new_node.count = len(new_node.data)

        node_to_split.data = node_to_split.data[:mid_point]
        node_to_split.count = len(node_to_split.data)

        new_node.next = node_to_split.next
        node_to_split.next = new_node

    def insert(self, value):
        if not self.__head:
            self.__head = Node(self.__node_capacity)
            self.__head.insert(value)
            return

        current = self.__head

        while current and value > current.data[-1]:
            if not current.next:
                break
            current = current.next

        if current.is_full():
            self.split_node(current)
            if value > current.data[-1]:
                current.next.insert(value)
            else:
                current.insert(value)
        else:
            current.insert(value)

    def remove(self, value):
        if not self.__head:
            return False

        current = self.__head
        previous = None

        while current and value not in current.data:
            previous = current
            current = current.next

        if not current:
            return False

        current.remove(value)

        if current.count == 0 and previous:
            previous.next = current.next

        if self.__head.count == 0:
            self.__head = self.__head.next

        return True

    def get_element_at(self, k):
        if not self.__head or k < 0:
            return None

        current = self.__head
        index_count = 0
        
        while current:
            if k < index_count + current.count:
                internal_index = k - index_count
                return current.data[internal_index]
            
            index_count = index_count + current.count
            current = current.next
            
        return None

    def total_elements(self):
        count = 0
        current = self.__head
        while current:
            count = count + current.count
            current = current.next
        return count

    def print_list(self):
        if not self.__head:
            print("Lista está vazia.")
            return

        current = self.__head
        node_index = 0
        while current:
            print(f"Nó {node_index}: (Itens: {current.count}) -> {current.data}")
            current = current.next
            node_index = node_index + 1