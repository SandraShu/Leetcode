#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 17:24:22 2017
@author: Sandra
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        l = self.ListNodeToList(head)
        del l[len(l)-n]
        a = self.ListToListNode(l)
        return a

    def ListNodeToList(self,head):
        l=[]
        while head.next:
            l.append(head.val)
            head = head.next
        l.append(head.val)
        return l

    def ListToListNode(self,l):
        
        if len(l)<1:
            return None

        node = ListNode(l[0])   
        for i in range(1,len(l)):
            self.appendNode(node,ListNode(l[i]))

        return node
    
    def appendNode(self,node,target):
        while node.next:
            node = node.next
        node.next = target
        
if __name__ == '__main__':

    # a = ListNode(1)
    # a.next = ListNode(2)
    # a.next.next = ListNode(3)
    # a.next.next.next = ListNode(4)
    # a.next.next.next.next = ListNode(5)

    s = Solution()
    l = [1]
    a = s.ListToListNode(l)
    result = s.removeNthFromEnd(a,1)