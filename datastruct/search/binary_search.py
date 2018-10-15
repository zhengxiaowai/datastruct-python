#!/usr/bin/env python
# -*- coding:utf-8 -*-


def binary_search(arr, target):
    if arr:
        return _binary_search(arr, target, 0, len(arr) -1)


def _binary_search(arr, target, start, end):
    if start > end or len(arr) == 0:
        return

    mid = (start + end) // 2
    if arr[mid] == target:
        return target

    if target < arr[mid]:
        return _binary_search(arr, target, start, mid - 1)
    else:
        return _binary_search(arr, target, mid + 1, end)