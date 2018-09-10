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
        if pos < 0 or pos > self._length:
            raise PositionError("pos error, 0 < pos < {}".format(self._length))

        if pos == 0:
            return self._head
        elif pos == self._length:
            return self.tail
        else:
            current_node = self._head
            for _ in range(pos):
                current_node = current_node.next
            return current_node

    def __setitem__(self, pos, node):
        if not isinstance(node, DNode):
            raise TypeError("node must a DNode")

        if self._head is None and self._tail is None:
            # insert a empty list
            self._head = node
            self._tail = node

            self._head.prev, self._tail.next = self._tail, self._head
        else:
            if pos == 0:
                # insert head
                node.next = self.head
                self.head.prev = node
                self._head = node

                self._head.prev, self._tail.next = self._tail, self._head
            elif pos == self._length:
                # insert tail
                self._tail.next = node
                node.prev = self._tail
                self._tail = node

                self._head.prev, self._tail.next = self._tail, self._head
            else:
                # insert middle
                current_node = self.search(pos)
                node.next = current_node
                node.prev = current_node.prev
                current_node.prev.next = node
                current_node.prev = node

        self._length += 1

    def __delitem__(self, pos):
        if self._head is None and self._tail is None:
            return

        current_node = self.search(pos)
        if current_node is self._head:
            if current_node.next is None:
                # only one node
                self._head = None
                self._tail = None
            else:
                current_node.next.prev = None
                self._head = current_node.next

                self._head.prev, self._tail.next = self._tail, self._head
        elif current_node is self._tail:
            current_node.prev.next = None
            self._tail = current_node.prev

            self._head.prev, self._tail.next = self._tail, self._head
        else:
            current_node.prev.next = current_node.next
            current_node.next.prev = current_node.prev

        self._length -= 1

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


