#!/usr/bin/env python
# -*- coding:utf-8 -*-


def max_heap_sort(arr):
    arr = build_max_heap(arr)
    capacity = len(arr)
    for i in range(len(arr), 1, -1):
        last = i - 1
        arr[0], arr[last] = arr[last], arr[0]

        capacity -= 1
        max_heapify(arr, 1, capacity)

    return arr


def build_max_heap(arr):
    for i in range(len(arr) // 2, 0, -1):
        max_heapify(arr, i, len(arr))

    return arr


def max_heapify(arr, i, capacity):
    left = 2 * i
    right = left + 1
    # capacity = len(arr) + 1
    max = i

    if left <= capacity and arr[left - 1] > arr[i - 1]:
        max = left

    if right <= capacity and arr[right - 1] > arr[max - 1]:
        max = right

    if max != i:
        arr[i - 1], arr[max - 1] = arr[max - 1], arr[i - 1]
        max_heapify(arr, max, capacity)


if __name__ == '__main__':
    arr = max_heap_sort([3, 4, 5, 1, 2])
    print(arr)