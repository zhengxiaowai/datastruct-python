#!/usr/bin/env python
# -*- coding:utf-8 -*-


from datastruct.list.node import SNode


def reverse_order_output(head, res=None):
    if head is None:
        return []

    if res is None:
        res = []

    res = reverse_order_output(head.next, res)
    res.append(head.value)

    return res


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


def merge_lists(l1_head, l2_head):
    dummy = cur = SNode(0)
    while l1_head and l2_head:
        if l1_head.value <= l2_head.value:
            cur.next = l1_head
            l1_head = l1_head.next
        else:
            cur.next = l2_head
            l2_head = l2_head.next
        cur = cur.next

    if l1_head:
        cur.next = l1_head

    if l2_head:
        cur.next = l2_head

    return dummy.next


def remove_nth_from_end(head, n):
    temp_head = head
    fast = head
    slow = head

    while fast is not None and n > -1:
        fast = fast.next
        n -= 1

    while fast is not None:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next
    return temp_head


def find_middle(head):
    fast = head
    slow = head

    while fast.next is not None and fast.next.next is not None:
        fast = fast.next.next
        slow = slow.next

    return slow