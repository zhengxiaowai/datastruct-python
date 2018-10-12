#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
from datastruct.list.slist import SinglyList, SNode
from datastruct.list.opt import reverse_order_output, find_intersection, \
    merge_lists, remove_nth_from_end, find_middle


class TestLinkedListOpt(unittest.TestCase):
    def test_reverse_order_output(self):
        sl = SinglyList([0, 1, 2, 3, 4, 5])
        self.assertEqual([5, 4, 3, 2, 1, 0], reverse_order_output(sl.head))

    def test_find_intersection(self):
        node0 = SNode(0)
        node11 = SNode(1)
        node12 = SNode(2)
        node21 = SNode(1)
        node22 = SNode(2)
        node3 = SNode(3)
        node4 = SNode(4)
        node5 = SNode(5)

        # 0 - 1(1) - 2(1) - 3 - 4 - 5
        node0.next = node11
        node11.next = node12
        node12.next = node3

        # 1(2) - 2(2) - 3 - 4 - 5
        node21.next = node22
        node22.next = node3

        node3.next = node4
        node4.next = node5

        sl1 = SinglyList()
        sl1._head = node0
        sl1._length = 6

        sl2 = SinglyList()
        sl2._head = node21
        sl2._length = 5

        self.assertIs(node3, find_intersection(sl1, sl2))

    def test_merge_lists(self):
        sl1 = SinglyList([1, 3, 5])
        sl2 = SinglyList([2, 4, 6, 8, 10])

        new_head = merge_lists(sl1.head, sl2.head)
        self.assertEqual([1, 2, 3, 4, 5, 6, 8, 10], SinglyList.traverse(new_head))

    def test_remove_eth_elem(self):
        sl = SinglyList([1, 2, 3, 4, 5])
        h = remove_nth_from_end(sl.head, 2)

        self.assertEqual([1, 2, 3, 5], SinglyList.traverse(h))

    def test_find_middle(self):
        sl = SinglyList([1, 2, 3, 4, 5])
        self.assertEqual(3, find_middle(sl.head).value)

        sl = SinglyList([1, 2, 3, 4, 5, 6])
        self.assertEqual(3, find_middle(sl.head).value)
