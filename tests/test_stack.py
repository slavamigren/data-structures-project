import unittest
from src.stack import Stack, Node

class TestNode(unittest.TestCase):
    def test_init(self):
        # Пишем нужное количество проверок
        self.assertEqual(Node(5, None).data, 5)
        self.assertEqual(Node(5, None).next_node, None)


class TestStack(unittest.TestCase):
    def test_init(self):
        self.assertEqual(Stack().top, None)

    def test_push(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        stack.push('data3')
        self.assertEqual(stack.top.data, 'data3')
        self.assertEqual(stack.top.next_node.data, 'data2')
        self.assertEqual(stack.top.next_node.next_node.data, 'data1')


    def test_pop(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        stack.push('data3')
        self.assertEqual(stack.pop(), 'data3')
        self.assertEqual(stack.pop(), 'data2')
        self.assertEqual(stack.pop(), 'data1')
        self.assertEqual(stack.pop(), None)

