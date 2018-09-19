#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
from datastruct.tree.avl import AVLTree


class TestAVLTreeTest(unittest.TestCase):
    def test_insert(self):
        avl = AVLTree()

        for i in range(5):
            avl.insert(i)

        self.assertEqual(avl.root.key, 1)
        self.assertEqual(avl.root.left.key, 0)
        self.assertEqual(avl.root.right.key, 3)
        self.assertEqual(avl.root.right.left.key, 2)
        self.assertEqual(avl.root.right.right.key, 4)
