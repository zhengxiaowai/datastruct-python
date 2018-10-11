#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
二叉查找树
"""


class BitNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return "Node({!r})".format(self.value)


def check_type(ins, ins_type):
    if isinstance(ins, ins_type):
        raise TypeError("need the instance of {}".format(ins_type))


def is_bst(root):
    pass


def minimum(root):
    return minimum(root.left) if root.left else root


def maximum(root):
    return minimum(root.right) if root.right else root


def successor(root, node):
    """ 后继既是右子树的最小值 """
    pass


def predecessor(root, node):
    """ 前驱既是左子树的最大值 """
    pass


def pre_order(root, res=None):
    if root is None:
        return []
    if res is None:
        res = []

    res.append(root.value)
    pre_order(root.left, res)
    pre_order(root.right, res)

    return res


def in_order(root, res=None):
    if root is None:
        return []
    if res is None:
        res = []

    in_order(root.left, res)
    res.append(root.value)
    in_order(root.right, res)

    return res


def post_order(root, res=None):
    if root is None:
        return []
    if res is None:
        res = []

    post_order(root.left, res)
    post_order(root.right, res)
    res.append(root.value)

    return res


def recur_search(root, value):
    if root is None:
        return None

    if root.value == value:
        return root

    if value < root.value:
        return recur_search(root.left, value)
    else:
        return recur_search(root.right, value)


def recur_insert(root, value):
    if root.value == value:
        return

    if value < root.value:
        # go to left
        if root.left:
            return recur_insert(root.left, value)
        else:
            root.left = BitNode(value)
            return
    else:
        # go to right
        if root.right:
            return recur_insert(root.right, value)
        else:
            root.right = BitNode(value)
            return


def recur_delete(root, value):
    if root is None:
        return

    if value < root.value:
        root.left = recur_delete(root.left, value)

    if value > root.value:
        root.right = recur_delete(root.right, value)

    if value == root.value:
        if root.left is None:
            return root.right

        if root.right is None:
            return root.left

        min_node = root.right
        p = None
        while min_node.left is not None:
            p = min_node
            min_node = min_node.left

        min_node.left = root.left
        if p:
            p.left = min_node.right
            min_node.right = root.right

        return min_node


def min_depth(root):
    if not root:
        return 0

    left_depth = min_depth(root.left)
    right_depth = min_depth(root.right)
    return 1 if (left_depth + right_depth) == 0 else min(left_depth, right_depth) + 1


def max_depth(root):
    if not root:
        return 0

    return max(max_depth(root.left), max_depth(root.right)) + 1


class BST:
    def __init__(self, value=None):
        if value:
            self._root = BitNode(value)

    @property
    def root(self):
        return self._root

    def insert(self, value):
        if self._root:
            recur_insert(self._root, value)
        else:
            self._root = BitNode(value)

    def search(self, value):
        return recur_search(self._root, value)

    def delete(self, value):
        return recur_delete(self._root, value)

    def pre_order(self):
        return pre_order(self._root)

    def in_order(self):
        return in_order(self._root)

    def post_order(self):
        return post_order(self._root)