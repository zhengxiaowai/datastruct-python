#!/usr/bin/env python
# -*- coding:utf-8 -*-


class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 0
        self.left = None
        self.right = None

    def __repr__(self):
        return "AVLNode({!r})".format(self.key)


class AVLTree:
    def __init__(self):
        self.root = None

    def node_height(self, node):
        return node.height if node else -1

    def update_height(self, node):
        node.height = max(self.node_height(node.left), self.node_height(node.right)) + 1

    def is_not_balance(self, node):
        return abs(self.node_height(node.left) - self.node_height(node.right)) > 1

    def ll_rotate(self, node):
        left_node = node.left
        node.left = left_node.right
        left_node.right = node

        self.update_height(node)
        self.update_height(left_node)

        return left_node

    def rr_rotate(self, node):
        right_node = node.right
        node.right = right_node.left
        right_node.left = node

        self.update_height(node)
        self.update_height(right_node)

        return right_node

    def lr_rotate(self, node):
        node.left = self.rr_rotate(node.left)
        return self.ll_rotate(node)

    def rl_rotate(self, node):
        node.right = self.ll_rotate(node.right)
        return self.rr_rotate(node)

    def insert(self, key):
        if self.root is None:
            self.root = AVLNode(key)
        else:
            self.root = self._insert(key, self.root)

    def _insert(self, key, node):
        if node is None:
            return AVLNode(key)

        if key < node.key:
            # 插入左边
            node.left = self._insert(key, node.left)
            if self.is_not_balance(node):
                if key < node.left.key:
                    # 左边的左边
                    node = self.ll_rotate(node)
                else:
                    # 左边的右边
                    node = self.lr_rotate(node)
        else:
            # 插入右边
            node.right = self._insert(key, node.right)
            if self.is_not_balance(node):
                if key > node.right.key:
                    # 右边的右边
                    node = self.rr_rotate(node)
                else:
                    # 右边的左边
                    node = self.rl_rotate(node)

        self.update_height(node)
        return node