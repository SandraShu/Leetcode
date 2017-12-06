#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 20:03:54 2017

@author: Sandra
"""
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle) 
        # 状态转移方程: triangle[i][j] += min(triangle[i+1][j+1],triangle[i+1][j]) 
        for i in range(n - 2, -1, -1):
            for j in range(i+1):          
                triangle[i][j] += min(triangle[i+1][j+1],triangle[i+1][j])    
        
        return triangle[0][0]

            
if __name__ == '__main__':
    s = Solution()
    #l=[[2],[3,4],[6,5,7],[4,1,8,3]]
    l=[[-1],[3,2],[-3,1,-1]]
    print(s.minimumTotal(l))
