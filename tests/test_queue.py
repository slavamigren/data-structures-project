import unittest
from src.queue import Queue, Node


class TestNode(unittest.TestCase):
    def test_init(self):
        self.assertEqual(Node(5, None).data, 5)
        self.assertEqual(Node(5, None).next_node, None)


class TestQueue(unittest.TestCase):
    def test_init(self):
        self.assertEqual(Queue().tail, None)
        self.assertEqual(Queue().head, None)


    def test__str__(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')
        self.assertEqual(str(queue), 'data1\ndata2\ndata3')


    def test_enqueue(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')
        self.assertEqual(queue.head.data, 'data1')
        self.assertEqual(queue.head.next_node.data, 'data2')
        self.assertEqual(queue.tail.data, 'data3')