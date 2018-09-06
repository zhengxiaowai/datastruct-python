#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
双向循环链表
"""

from datastruct.list.node import DNode
from datastruct.list.exceptions import PositionError


class CircularDoublyList:
    def __init__(self, nodes=None):
        self._length = len(nodes) if nodes else 0
        self._head = None
        self._tail = None

        if nodes:
            if len(nodes) < 1:
                raise ValueError("nodes must contain at least one DNode")

            for node in nodes:
                if not isinstance(node, DNode):
                    raise TypeError("{!r} is not DNode")

            self._head = nodes[0]
            current_node = self._head
            for node in nodes[1:]:
                current_node.next = node
                node.prev = current_node
                current_node = current_node.next

            self._tail = current_node
            self._head.prev = self._tail
            self._tail.next = self._head

    def __len__(self):
        return self._length

    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail

    def search(self, pos):
        return self.__getitem__(pos)

    def insert(self, pos, node):
        self.__setitem__(pos, node)

    def delete(self, pos):
        self.__delitem__(pos)

    def __getitem__(self, pos):
        pass

    def __setitem__(self, pos, node):
        pass

    def __delitem__(self, pos):
        pass

    def values(self):
        values = []
        if self._length == 0:
            return values

        current_node = self.head
        while True:
            values.append(current_node)
            current_node = current_node.next
            if current_node is self._head:
                break
        return values


