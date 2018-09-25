#!/usr/bin/env python
# -*- coding:utf-8 -*


def shell_sort(arr):
    gap = 1
    while gap < (len(arr) // 3):
        gap = gap * 3 + 1 # 1, 4, 13, 40 ...

    while gap >= 1:
        for i in range(gap, len(arr), gap):
            curr = arr[i]
            pre_index = i - gap

            while pre_index >= 0 and curr < arr[pre_index]:
                arr[pre_index + gap] = arr[pre_index]
                pre_index -= gap
            arr[pre_index + gap] = curr
        gap = gap // 3

    return arr
