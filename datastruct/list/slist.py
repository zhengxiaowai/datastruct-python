#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
单向链表实现
"""

from datastruct.list.node import SNode


class PositionError(Exception):
    pass


class EmptyError(Exception):
    pass


class SinglyList:
    def __init__(self, values=None):
        self._length = len(values) if values else 0
        self._head = None

        # 初始化 values，转换成 SNode 链表
        if values:
            self._head = SNode(values[0])
            current_node = self._head
            for value in values[1:]:
                current_node.next = SNode(value)
                current_node = current_node.next

    @property
    def head(self):
        return self._head

    def __len__(self):
        return self._length

    def __str__(self):
        return "SinglyList: {!r}".format(self.values())

    def __repr__(self):
        return "SinglyList({!r})".format(self.values())

    def __getitem__(self, pos):
        if self._length == 0:
            raise EmptyError("list's length is 0, can not do search")

        if pos > self._length or pos < 0:
            raise PositionError("invalid position, must <= length")

        current_node = self._head
        for _ in range(pos):
            current_node = current_node.next

        return current_node

    def __setitem__(self, pos, new_node):
        if not isinstance(new_node, SNode):
            raise TypeError("new_node need a SNode isinstance")

        if pos > self._length:
            raise PositionError("invalid position, must <= length")

        # 单链表插入 new_node 步骤
        if pos == 0:
            # 如果是头节点
            if not self._head:
                # 空列表
                self._head = new_node
            else:
                new_node.next = self._head
                self._head = new_node
        else:
            prev_node = self.search(pos - 1)
            new_node.next = prev_node.next
            prev_node.next = new_node

        self._length += 1

    def __delitem__(self, pos):
        if pos < 0 or pos > self._length:
            raise PositionError("position is in invalid interval, must 0 < pos < {}".format(self._length))

        if pos == 0:
            self._head = self._head.next
        elif 0 < pos < self._length:
            prev_node = self.search(pos - 1)
            prev_node.next = prev_node.next.next
        else:
            # pos == self._length
            prev_node = self.search(pos - 1)
            prev_node.next = None

        self._length -= 1

    def __reversed__(self):
        list_head = self._head
        result = None

        while list_head:
            temp = list_head.next
            list_head.next = result
            result = list_head
            list_head = temp

        self._head = result

    def is_loop(self):
        fast = self._head
        slow = self.head

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                return True
        return False

    def values(self):
        values = []
        current_node = self._head
        while current_node is not None:
            values.append(current_node.value)
            current_node = current_node.next

        return values

    def search(self, pos):
        return self.__getitem__(pos)

    def insert(self, pos, new_node):
        self.__setitem__(pos, new_node)

    def delete(self, pos):
        self.__delitem__(pos)

    @staticmethod
    def find_intersection(list1, list2):
        diff = len(list1) - len(list2)
        head1 = list1.head
        head2 = list2.head

        if diff < 0:
            # len1 < len2
            for _ in range(diff*-1):
                head2 = head2.next
        elif diff > 0:
            # len1 > len2
            for _ in range(diff):
                head1 = head1.next
        else:
            pass

        while head1 is not None and head2 is not None and head1 is not head2:
            head1 = head1.next
            head2 = head2.next

        return head1 if head1 is head2 else None




