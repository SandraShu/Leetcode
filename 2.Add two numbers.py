#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 14:35:44 2017

@author: Sandra
"""

# Definition for singly-linked list.
class ListNode(object):
    
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
        
    def node_to_list(self,l):      
        result = []   
        while l is not None:  
            result.append(l.val)
            l = l.next 
        return result
            
    def addTwoNumbers(self, l1, l2):
        
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        l1 = self.node_to_list(l1)
        l2 = self.node_to_list(l2)
        
        a = 0
        for i in range(len(l1)):
            a = a + l1[i] * 10 ** i
                       
        b = 0
        for i in range(len(l2)):
            b = b + l2[i] * 10 ** i

        c = str(a + b)
        
        head = ListNode(int(c[0]))
        for i in range(1,len(c)):
            n = ListNode(int(c[i]))
            n.next = head
            head = n
        
        # print(self.node_to_list(head))
        return head
                     
if __name__ == '__main__':
    
    l1 = ListNode(2)
    l1.next = ListNode(4)
    # l1.next.next = ListNode(3)
    
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
       
    s = Solution()
    result = s.addTwoNumbers(l1, l2)
    # print(result)
