#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest

from datastruct.tree.bst import pre_order, in_order, post_order, \
    recur_insert, recur_search, recur_delete, BitNode, min_depth, \
    max_depth


class TestRecurBST(unittest.TestCase):
    def test_pre_order(self):
        n1 = BitNode(10)
        n2 = BitNode(5)
        n3 = BitNode(15)
        n4 = BitNode(3)
        n5 = BitNode(13)
        n6 = BitNode(16)

        n1.left, n1.right = n2, n3
        n2.left, n2.right = n4, None
        n3.left, n3.right = n5, n6

        self.assertEqual([10, 5, 3, 15, 13, 16], pre_order(n1))

    def test_in_order(self):
        n1 = BitNode(10)
        n2 = BitNode(5)
        n3 = BitNode(15)
        n4 = BitNode(3)
        n5 = BitNode(13)
        n6 = BitNode(16)

        n1.left, n1.right = n2, n3
        n2.left, n2.right = n4, None
        n3.left, n3.right = n5, n6
        self.assertEqual([3, 5, 10, 13, 15, 16], in_order(n1))

    def test_post_order(self):
        n1 = BitNode(10)
        n2 = BitNode(5)
        n3 = BitNode(15)
        n4 = BitNode(3)
        n5 = BitNode(13)
        n6 = BitNode(16)

        n1.left, n1.right = n2, n3
        n2.left, n2.right = n4, None
        n3.left, n3.right = n5, n6
        self.assertEqual([3, 5, 13, 16, 15, 10], post_order(n1))

    def test_insert(self):
        n1 = BitNode(10)

        recur_insert(n1, 5)
        recur_insert(n1, 15)
        recur_insert(n1, 3)
        recur_insert(n1, 13)
        recur_insert(n1, 16)

        self.assertEqual(n1.value, 10)
        self.assertEqual(n1.left.value, 5)
        self.assertEqual(n1.left.left.value, 3)
        self.assertEqual(n1.right.value, 15)
        self.assertEqual(n1.right.left.value, 13)
        self.assertEqual(n1.right.right.value, 16)

    def test_search(self):
        n1 = BitNode(10)
        n2 = BitNode(5)
        n3 = BitNode(15)
        n4 = BitNode(3)
        n5 = BitNode(13)
        n6 = BitNode(16)

        n1.left, n1.right = n2, n3
        n2.left, n2.right = n4, None
        n3.left, n3.right = n5, n6

        self.assertIs(recur_search(n1, 10), n1)
        self.assertIs(recur_search(n1, 5), n2)
        self.assertIs(recur_search(n1, 15), n3)
        self.assertIs(recur_search(n1, 3), n4)
        self.assertIs(recur_search(n1, 13), n5)
        self.assertIs(recur_search(n1, 16), n6)

    def test_delete(self):
        n1 = BitNode(20)
        n2 = BitNode(10)
        n3 = BitNode(30)
        n4 = BitNode(5)
        n5 = BitNode(15)
        n6 = BitNode(2)
        n7 = BitNode(12)
        n8 = BitNode(13)

        n1.left, n1.right = n2, n3
        n2.left, n2.right = n4, n5
        n4.left, n4.right = None, n6
        n5.left, n5.right = n7, None
        n7.left, n7.right = None, n8

        recur_delete(n1, 10)
        self.assertEqual([5, 2, 12, 13, 15, 20, 30], in_order(n1))


class TestBSTProperty(unittest.TestCase):
    def test_depth(self):
        n1 = BitNode(20)
        n2 = BitNode(10)
        n3 = BitNode(30)
        n4 = BitNode(5)
        n5 = BitNode(15)
        n6 = BitNode(2)
        n7 = BitNode(12)

        n1.left, n1.right = n2, n3
        n2.left, n2.right = n4, n5
        n4.left, n4.right = n6, None
        n5.left, n5.right = n7, None

        self.assertEqual(2, min_depth(n1))
        self.assertEqual(4, max_depth(n1))



