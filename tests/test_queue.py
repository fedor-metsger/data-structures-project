"""Здесь надо написать тесты с использованием unittest для модуля queue."""

"""Здесь надо написать тесты с использованием unittest для модуля stack."""

import unittest
from src.queue import Queue

class TestQueue(unittest.TestCase):
    """
    Класс для тестирования класса Stack
    """
    def test_init(self):
        """Тестирует метод Stack.__init__()"""
        queue = Queue()
        self.assertEqual(queue.head, None)
        self.assertEqual(queue.tail, None)

    def test_enqueue(self):
        queue = Queue()
        queue.enqueue("data1")
        self.assertEqual(queue.head.data, "data1")
        self.assertEqual(queue.tail.data, "data1")
        queue.enqueue("data2")
        self.assertEqual(queue.head.data, "data1")
        self.assertEqual(queue.tail.data, "data2")

    def test_dequeue(self):
        queue = Queue()
        queue.enqueue("data1")
        queue.enqueue("data2")
        self.assertEqual(queue.dequeue(), "data1")
        self.assertEqual(queue.dequeue(), "data2")
        self.assertEqual(queue.dequeue(), None)

    def test_str(self):
        queue = Queue()
        self.assertEqual(queue.__str__(), "")
        queue.enqueue("data1")
        queue.enqueue("data2")
        queue.enqueue("data3")
        self.assertEqual(queue.__str__(), "data1\ndata2\ndata3")