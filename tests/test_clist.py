#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
from datastruct.list.clist import CircularDoublyList
from datastruct.list.node import DNode


class TestDoublyList(unittest.TestCase):
    def test_create_clist(self):
        cl = CircularDoublyList()
        self.assertEqual(len(cl), 0)
        self.assertIsNone(cl.head)
        self.assertIsNone(cl.tail)

        node0 = DNode(0)
        cl = CircularDoublyList([node0])
        self.assertEqual(len(cl), 1)
        self.assertIs(cl.head, node0)
        self.assertIs(cl.tail, node0)
        self.assertIs(cl.head.next, node0)
        self.assertIs(cl.head.prev, node0)
        self.assertIs(cl.tail.next, node0)
        self.assertIs(cl.tail.prev, node0)

        node0 = DNode(0)
        node1 = DNode(1)
        node2 = DNode(2)
        node3 = DNode(3)
        cl = CircularDoublyList([node0, node1, node2, node3])
        self.assertEqual(len(cl), 4)
        self.assertIs(cl.head, node0)
        self.assertIs(cl.head.next, node1)
        self.assertIs(cl.head.next.next, node2)
        self.assertIs(cl.head.next.next.next, node3)
        self.assertIs(cl.head.next.next.next.next, node0)
        self.assertIs(cl.tail, node3)
        self.assertIs(cl.tail.prev, node2)
        self.assertIs(cl.tail.prev.prev, node1)
        self.assertIs(cl.tail.prev.prev.prev, node0)
        self.assertIs(cl.tail.prev.prev.prev.prev, node3)

    def test_insert_clist(self):
        node0 = DNode(0)
        node1 = DNode(1)
        node2 = DNode(2)
        node3 = DNode(3)
        cl = CircularDoublyList()

        cl.insert(0, node0)
        self.assertEqual(len(cl), 1)
        self.assertIs(cl.head, node0)
        self.assertIs(cl.tail, node0)
        self.assertIs(cl.head.prev, cl.tail)
        self.assertIs(cl.tail.next, cl.head)

        cl.insert(0, node1) # node1 node0
        self.assertEqual(len(cl), 2)
        self.assertIs(cl.head, node1)
        self.assertIs(cl.head.prev, cl.tail)
        self.assertIs(cl.head.next, node0)
        self.assertIs(cl.head.next.prev, node1)
        self.assertIs(cl.tail, node0)
        self.assertIs(cl.tail.next, cl.head)
        self.assertIs(cl.tail.prev, node1)
        self.assertIs(cl.tail.prev.next, node0)
        self.assertIs(cl.head.prev, cl.tail)
        self.assertIs(cl.tail.next, cl.head)

        cl.insert(2, node2) # node1 node0 node2
        self.assertEqual(len(cl), 3)
        self.assertIs(cl.head, node1)
        self.assertIs(cl.tail.next, cl.head)
        self.assertIs(cl.tail, node2)
        self.assertIs(cl.tail.prev, node0)
        self.assertIs(cl.tail.prev.next, node2)
        self.assertIs(cl.head.prev, cl.tail)
        self.assertIs(cl.tail.next, cl.head)

        cl.insert(2, node3)  # node1 node0 node3 node2
        self.assertEqual(len(cl), 4)
        self.assertIs(cl.tail.prev, node3)
        self.assertIs(cl.tail.prev.next, node2)
        self.assertIs(cl.tail.prev.prev, node0)
        self.assertIs(cl.tail.prev.prev.next, node3)
        self.assertIs(cl.head.prev, cl.tail)
        self.assertIs(cl.tail.next, cl.head)