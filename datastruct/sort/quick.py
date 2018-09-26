#!/usr/bin/env python
# -*- coding:utf-8 -*-


def quick_sort(arr, recur=True):
    quick_sort_iter(arr, 0, len(arr) - 1)
    if recur:
        quick_sort_recur(arr, 0, len(arr) - 1)
    else:
        quick_sort_iter(arr, 0, len(arr) - 1)


def quick_sort_recur(arr, first, last):
    if first < last:
        pivot = partition(arr, first, last)
        quick_sort_recur(arr, first, pivot - 1)
        quick_sort_recur(arr,  pivot + 1, last)


def quick_sort_iter(arr, first, last):
    stack = [0] * 4

    top = -1

    top += 1
    stack[top] = first

    top += 1
    stack[top] = last

    while top >= 0:
        h = stack[top]
        top -= 1
        l = stack[top]
        top -= 1

        p = partition(arr, l, h)

        if p - 1 > l:
            top += 1
            stack[top] = l
            top += 1
            stack[top] = p - 1

        if p + 1 < h:
            top += 1
            stack[top] = p + 1
            top += 1
            stack[top] = h


def partition(arr, first, last):
    # first is pivot
    wall = first + 1
    for pos in range(first + 1, last + 1):
        if arr[pos] < arr[first]:
            arr[pos], arr[wall] = arr[wall], arr[pos]
            wall += 1

    arr[first], arr[wall-1] = arr[wall-1], arr[first]
    return wall - 1

    # last is the pivot
    # wall = first
    # for pos in range(first, last):
    #     if arr[pos] < arr[last]:
    #         arr[pos], arr[wall] = arr[wall], arr[pos]
    #         wall += 1
    # arr[wall], arr[last] = arr[last], arr[wall]
    # return wall


if __name__ == '__main__':
    arr = [5, 6, 6, 8, 1, 3, 7]
    quick_sort(arr)
    print(arr)