"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""

import unittest
from src.linked_list import LinkedList, Node

class TestLinkedList(unittest.TestCase):
    """
    Класс для тестирования класса Stack
    """
    def test_init(self):
        """Тестирует метод Stack.__init__()"""
        llist = LinkedList()
        self.assertEqual(llist.head, None)
        self.assertEqual(llist.tail, None)

    def test_insert_head(self):
        llist = LinkedList()
        llist.insert_beginning("data1")
        self.assertEqual(llist.head.data, "data1")
        self.assertEqual(llist.tail.data, "data1")
        llist.insert_beginning("data2")
        self.assertEqual(llist.head.data, "data2")
        self.assertEqual(llist.tail.data, "data1")

    def test_insert_tail(self):
        llist = LinkedList()
        llist.insert_at_end("data1")
        self.assertEqual(llist.head.data, "data1")
        self.assertEqual(llist.tail.data, "data1")
        llist.insert_at_end("data2")
        self.assertEqual(llist.head.data, "data1")
        self.assertEqual(llist.tail.data, "data2")

    def test_str(self):
        llist = LinkedList()
        self.assertEqual(llist.__str__(), "None")
        llist.insert_beginning("data1")
        llist.insert_beginning("data2")
        llist.insert_beginning("data3")
        self.assertEqual(llist.__str__(), "data3 -> data2 -> data1 -> None")

    def test_node(self):
        node = Node('data1', None)
        self.assertEqual(node.data, 'data1')
        self.assertEqual(node.next_node, None)

    def test_to_list(self):
        llist = LinkedList()
        llist.insert_beginning("data1")
        llist.insert_beginning("data2")
        llist.insert_beginning("data3")
        self.assertEqual(llist.to_list(), ["data3", "data2", "data1"])

    def test_get_data_by_id(self):
        llist = LinkedList()
        llist.insert_beginning([1, "data1"])
        llist.insert_beginning("data2")
        llist.insert_beginning({"id": 3, "data": "data3"})
        self.assertEqual(llist.get_data_by_id(3), {"id": 3, "data": "data3"})