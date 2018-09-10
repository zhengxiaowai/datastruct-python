#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
from datastruct.list.dlist import DoublyList
from datastruct.list.node import DNode


class TestDoublyList(unittest.TestCase):
    def test_create_dlist(self):
        dl = DoublyList()
        self.assertEqual(len(dl), 0)
        self.assertIsNone(dl.head)
        self.assertIsNone(dl.tail)

        node0 = DNode(0)
        dl = DoublyList([node0])
        self.assertIs(dl.head, node0)
        self.assertIs(dl.tail, node0)

        node0 = DNode(0)
        node1 = DNode(1)
        node2 = DNode(2)
        dl = DoublyList([node0, node1, node2])
        self.assertIs(dl.head, node0)
        self.assertIs(dl.tail, node2)
        self.assertIsNone(dl.head.prev)
        self.assertIsNone(dl.tail.next)

        self.assertIs(dl.head.next, node1)
        self.assertIs(dl.head.next.next, node2)
        self.assertIs(dl.tail.prev, node1)
        self.assertIs(dl.tail.prev.prev, node0)

    def test_insert_node(self):
        node0 = DNode(0)
        node1 = DNode(1)
        node2 = DNode(2)
        node3 = DNode(3)
        dl = DoublyList()

        dl.insert(0, node0)
        self.assertEqual(len(dl), 1)
        self.assertIs(dl.head, node0)
        self.assertIs(dl.tail, node0)

        dl.insert(0, node1) # node1 node0
        self.assertEqual(len(dl), 2)
        self.assertIs(dl.head, node1)
        self.assertIsNone(dl.head.prev)
        self.assertIs(dl.head.next, node0)
        self.assertIs(dl.head.next.prev, node1)
        self.assertIs(dl.tail, node0)
        self.assertIsNone(dl.tail.next)
        self.assertIs(dl.tail.prev, node1)
        self.assertIs(dl.tail.prev.next, node0)

        dl.insert(2, node2) # node1 node0 node2
        self.assertEqual(len(dl), 3)
        self.assertIs(dl.head, node1)
        self.assertIsNone(dl.tail.next)
        self.assertIs(dl.tail, node2)
        self.assertIs(dl.tail.prev, node0)
        self.assertIs(dl.tail.prev.next, node2)

        dl.insert(2, node3)  # node1 node0 node3 node2
        self.assertEqual(len(dl), 4)
        self.assertIs(dl.tail.prev, node3)
        self.assertIs(dl.tail.prev.next, node2)
        self.assertIs(dl.tail.prev.prev, node0)
        self.assertIs(dl.tail.prev.prev.next, node3)

    def test_search_node(self):
        node0 = DNode(0)
        node1 = DNode(1)
        node2 = DNode(2)
        node3 = DNode(3)
        dl = DoublyList([node0, node1, node2, node3])
        self.assertIs(dl.search(0), node0)
        self.assertIs(dl.search(1), node1)
        self.assertIs(dl.search(2), node2)
        self.assertIs(dl.search(3), node3)

    def test_delete_node(self):
        node0 = DNode(0)
        node1 = DNode(1)
        node2 = DNode(2)
        node3 = DNode(3)
        dl = DoublyList([node0, node1, node2, node3])
        dl.delete(2)
        self.assertIsNot(dl.head.next.next, node2)
        self.assertEqual(len(dl), 3)

        dl.delete(0)
        self.assertIs(dl.head, node1)
        self.assertEqual(len(dl), 2)

        dl.delete(2)
        self.assertIs(dl.tail, node1)
        self.assertEqual(len(dl), 1)