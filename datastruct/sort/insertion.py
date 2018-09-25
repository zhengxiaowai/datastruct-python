#!/usr/bin/env python
# -*- coding:utf-8 -*-


def insertion_sort(arr):
    for i in range(1, len(arr)):
        pre_index = i - 1
        curr = arr[i]

        while pre_index >= 0 and curr < arr[pre_index]:
            arr[pre_index + 1] = arr[pre_index]
            pre_index -= 1

        arr[pre_index + 1] = curr
    return arr

