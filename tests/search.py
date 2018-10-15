#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
from datastruct.search.binary_search import binary_search


class TestSearch(unittest.TestCase):
    def setUp(self):
        self.table_test_cast = [
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3),
            ([1, 2, 3], 1),
            ([1, 2], 2),
            ([], None)
        ]

    def test_binary_search(self):
        for case in self.table_test_cast:
            self.assertEqual(case[1], binary_search(case[0], case[1]))