
"""Здесь надо написать тесты с использованием unittest для модуля stack."""

import unittest
from src.stack import Stack

class TestStack(unittest.TestCase):
    """
    Класс для тестирования класса Stack
    """
    def test_init(self):
        """Тестирует метод Stack.__init__()"""
        stack = Stack()
        self.assertEqual(stack.top, None)

    def test_push(self):
        stack = Stack()
        self.assertEqual(stack.top, None)
        stack.push("data1")
        self.assertEqual(stack.top.data, "data1")

    def test_pop(self):
        stack = Stack()
        self.assertEqual(stack.pop(), None)
        stack.push("data1")
        self.assertEqual(stack.pop(), "data1")
