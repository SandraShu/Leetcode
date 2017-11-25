#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 18:08:07 2017

@author: Sandra
"""

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        # 初始化n*n矩阵
        matrix = [[0]*n for i in range(n)]
        # 起始数字
        num = 1
        # 按轮数循环
        for r in range(n/2):
            # 填充本轮第1行数据 正向 [r,n-r)
            for j in range(r,n-r):
                matrix[r][j] = num
                num += 1
            # 填充本轮最后1列数据 正向 [r+1,n-r)
            for i in range(r+1,n-r):
                matrix[i][n-r-1] = num
                num += 1
            # 填充本轮最后1行数据 反向 [n-r-2,r-1)
            for j in range(n-r-2,r-1,-1):
                matrix[n-r-1][j] = num
                num += 1
            # 填充本轮第1列数据 反向 [n-r-2,r)
            for i in range(n-r-2,r,-1):
                matrix[i][r] = num
                num += 1
        
        # n为奇数，填充矩阵中间数字
        if n%2 == 1:
            matrix[n/2][n/2] = num
                
        return matrix

if __name__ == '__main__':

    s = Solution()
    result = s.generateMatrix(2)
    print(result)