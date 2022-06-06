#!/usr/bin/env python3
# https://leetcode.com/problems/intersection-of-two-linked-lists/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        intersect_val = None
        intersected = False

        tmpA = headA
        tmpB = headB

        while tmpA.next and tmpB.next:
            tmpA = tmpA.next
            tmpB = tmpB.next

        if tmpA.next:
            while tmpA.next:
                headA = headA.next
                tmpA = tmpA.next
        elif tmpB.next:
            while tmpB.next:
                headB = headB.next
                tmpB = tmpB.next

        if headA == headB:
            intersect_val = headA
            intersected = True

        while headA.next:
            headA = headA.next
            headB = headB.next
            if headA != headB:
                intersected = False
                intersect_val = None
            elif not intersected:
                intersect_val = headA
                intersected = True

        return intersect_val
