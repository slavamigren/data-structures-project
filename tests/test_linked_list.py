import unittest
from src.linked_list import LinkedList, Node


class TestNode(unittest.TestCase):
    def test_init(self):
        self.assertEqual(Node(5, None).data, 5)
        self.assertEqual(Node(5, None).next_node, None)


class TestLinkedList(unittest.TestCase):
    def test_init(self):
        self.assertEqual(LinkedList().head, None)

    def test_insert_beginning(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        self.assertEqual(ll.head.data, {'id': 1})
        ll.insert_beginning({'id': 2})
        self.assertEqual(ll.head.data, {'id': 2})

    def test_insert_at_end(self):
        ll = LinkedList()
        ll.insert_at_end({'id': 0})
        self.assertEqual(ll.head.data, {'id': 0})
        ll.insert_at_end({'id': 1})
        ll.insert_at_end({'id': 2})
        self.assertEqual(ll.head.next_node.next_node.data, {'id': 2})

    def test__str__(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        ll.insert_at_end({'id': 2})
        ll.insert_at_end({'id': 3})
        ll.insert_beginning({'id': 0})
        self.assertEqual(str(ll), " {'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None")


