#!/usr/bin/env python
# -*- coding:utf-8 -*-


def bubble_sort(arr):
    for i in range(0, len(arr) -1):
        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr
