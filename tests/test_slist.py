#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
from datastruct.list.node import SNode
from datastruct.list.slist import SinglyList


class TestSList(unittest.TestCase):
    def test_create_slist(self):
        sl = SinglyList()
        self.assertIsNone(sl.head)
        self.assertEqual(len(sl), 0)

        sl = SinglyList([0, 1, 2, 3])
        self.assertIsNotNone(sl.head)
        self.assertIs(len(sl), 4)
        self.assertEqual(sl.head.value, 0)
        self.assertEqual(sl.head.next.value, 1)
        self.assertEqual(sl.head.next.next.value, 2)
        self.assertEqual(sl.head.next.next.next.value, 3)

    def test_insert_node(self):
        sl = SinglyList()
        sl.insert(0, SNode(0))
        sl[1] = SNode(1)
        self.assertEqual(len(sl), 2)
        self.assertEqual(sl.head.value, 0)
        self.assertEqual(sl.head.next.value, 1)

        sl = SinglyList([0])
        sl.insert(0, SNode(1))
        sl[0] = SNode(2)
        self.assertEqual(len(sl), 3)
        self.assertEqual(sl.head.value, 2)
        self.assertEqual(sl.head.next.value, 1)
        self.assertEqual(sl.head.next.next.value, 0)

        sl = SinglyList([0, 3])
        sl.insert(1, SNode(1))
        sl[2] = SNode(2)
        self.assertEqual(len(sl), 4)
        self.assertEqual(sl.head.value, 0)
        self.assertEqual(sl.head.next.value, 1)
        self.assertEqual(sl.head.next.next.value, 2)
        self.assertEqual(sl.head.next.next.next.value, 3)

    def test_search_node(self):
        sl = SinglyList([0, 2, 4, 6])
        self.assertEqual(sl[0].value, 0)
        self.assertEqual(sl.search(1).value, 2)
        self.assertEqual(sl.search(2).value, 4)
        self.assertEqual(sl[3].value, 6)

    def test_delete_node(self):
        sl = SinglyList([0])
        sl.delete(0)
        self.assertEqual(len(sl), 0)
        self.assertIsNone(sl.head)

        sl = SinglyList([0, 1, 2])
        sl.delete(0)
        self.assertEqual(len(sl), 2)
        self.assertEqual(sl.head.value, 1)
        self.assertEqual(sl.head.next.value, 2)

        sl = SinglyList([0, 1, 2])
        sl.delete(1)
        self.assertEqual(len(sl), 2)
        self.assertEqual(sl.head.value, 0)
        self.assertEqual(sl.head.next.value, 2)

        sl = SinglyList([0, 1, 2])
        sl.delete(2)
        self.assertEqual(len(sl), 2)
        self.assertEqual(sl.head.value, 0)
        self.assertEqual(sl.head.next.value, 1)

    def test_reversed_list(self):
        sl = SinglyList([0, 1, 2, 3, 4])
        reversed(sl)
        self.assertEqual([4, 3, 2, 1, 0], sl.values())

    def test_is_loop(self):
        sl = SinglyList([0, 1, 2, 3, 4])
        self.assertEqual(sl.is_loop(), False)

        node1 = SNode(1)
        node2 = SNode(2)
        node3 = SNode(3)
        node4 = SNode(4)
        node5 = SNode(5)
        node6 = SNode(6)

        # make a loop
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5
        node5.next = node6
        node6.next = node3

        sl = SinglyList()
        sl._head = node1
        sl._length = 6

        self.assertEqual(sl.is_loop(), True)