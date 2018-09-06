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