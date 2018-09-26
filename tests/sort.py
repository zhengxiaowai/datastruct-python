#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest

from datastruct.sort.bubble import bubble_sort
from datastruct.sort.selection import selection_sort
from datastruct.sort.insertion import insertion_sort
from datastruct.sort.shell import shell_sort
from datastruct.sort.quick import quick_sort


class TestSort(unittest.TestCase):
    def setUp(self):
        self.table_test_cast = [
            ([5, 7, 9, 1, 3, 2, 4, 6, 8, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
            ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
            ([3, 4, 2, 5, 1], [1, 2, 3, 4, 5]),
            ([1, 0], [0, 1]),
            ([0, 1], [0, 1]),
            ([1], [1]),
            ([], [])
        ]

    def test_bubble_sort(self):
        for case in self.table_test_cast:
            self.assertEqual(case[1], bubble_sort(case[0]))

    def test_selection_sort(self):
        for case in self.table_test_cast:
            self.assertEqual(case[1], selection_sort(case[0]))

    def test_insertion_sort(self):
        for case in self.table_test_cast:
            self.assertEqual(case[1], insertion_sort(case[0]))

    def test_shell_sort(self):
        for case in self.table_test_cast:
            self.assertEqual(case[1], shell_sort(case[0]))

    def test_quick_sort(self):
        for case in self.table_test_cast:
            self.assertEqual(case[1], quick_sort(case[0]))
            self.assertEqual(case[1], quick_sort(case[0], True))