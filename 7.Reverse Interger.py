#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 10:34:44 2017

@author: Sandra
"""

class Solution(object):
    
    # int32判断，溢出返回0
    def int32(self,x):
        # 2^31
        if x>0x7FFFFFFF:
            return 0
        
        if x<-0x7FFFFFFF:
            return 0
    
        return x
    
    # 字符串反转
    def string_reverse(self,string):  
        return string[::-1]
    
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if x >= 0:
            return self.int32(int(self.string_reverse(str(x))))
        else:
            return self.int32(-int(self.string_reverse(str(abs(x)))))

if __name__ == '__main__':

    n = 1563847412
       
    s = Solution()
    result = s.reverse(n)
    print(result)