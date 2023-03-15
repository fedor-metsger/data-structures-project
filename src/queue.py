class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node

    def __str__(self):
        if self.next_node:
            return f"{self.data}\n{self.next_node}"
        return f"{self.data}"


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = self.tail = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        if self.tail:
            self.tail.next_node = Node(data, self.tail.next_node)
            self.tail = self.tail.next_node
        else:
            self.head = self.tail = Node(data, None)

    def __str__(self):
        if self.head: return str(self.head)
        else: return ""
        # n = self.head
        # lst = []
        # while n:
        #     lst.append(n.data)
        #     n = n.next_node
        # return '\n'.join(lst)

    def dequeue(self):
        """
        Метод для удаления элемента из очереди и его возвращения

        :return: данные удаленного элемента
        """
        pass
