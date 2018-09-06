#!/usr/bin/env python
# -*- coding:utf-8 -*-


class SNode:
    """
    单向链表节点
    """
    def __init__(self, value):
        self._value = value
        self.next = None

    @property
    def value(self):
        return self._value

    def __repr__(self):
        return "SNode({})".format(self._value)


class DNode(SNode):
    """
    双向链表节点
    """
    def __init__(self, value):
        super().__init__(value)
        self.prev = None

    def __repr__(self):
        return "DNode({!r})".format(self._value)

