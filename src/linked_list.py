class Node:
    """Класс для узла односвязного списка"""
    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""
    def __init__(self):
        """Конструктор класса LinkedList"""
        self.head = self.tail = None
    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        if self.head:
            self.head = Node(data, self.head)
        else:
            self.head = self.tail = Node(data, None)

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        if self.tail:
            self.tail.next_node = Node(data, None)
            self.tail = self.tail.next_node
        else:
            self.head = self.tail = Node(data, None)

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f'{str(node.data)} -> '
            node = node.next_node

        ll_string += 'None'
        return ll_string

    def to_list(self):
        lst, n = [], self.head
        while n:
            lst.append(n.data)
            n = n.next_node
        return lst

    def get_data_by_id(self, id):
        n = self.head
        while n:
            try:
                if n.data["id"] == id:
                    return n.data
            except TypeError as e:
                print("Данные не являются словарем или в словаре нет id")
            n = n.next_node
        return None
