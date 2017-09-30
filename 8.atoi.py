#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 18:44:28 2017

@author: Sandra
"""

class Solution(object):
    def myAtoi(self, s):
        """
        :type str: s
        :rtype: int
        """

        return int(s)
    
if __name__ == '__main__':
    
    ss = 'a123'
    
    s = Solution()
    result = s.myAtoi(ss)
    print(result)