#!/usr/bin/env python
# -*- coding:utf-8 -*-


def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right, [0] * len(arr))


def merge(left, right, merged):
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged[i+j] = left[i]
            i += 1
        else:
            merged[i + j] = right[j]
            j += 1

    while i < len(left):
        merged[i+j] = left[i]
        i += 1

    while j < len(right):
        merged[i + j] = right[j]
        j += 1

    return merged
