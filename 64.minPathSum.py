#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 21:59:22 2017
@author: Sandra
"""

class Solution(object):
    def minPathSum1(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        if m < 1 or n < 1:
            return 0

        minLen = [grid[0][0]]
        #首先每一个路径的上一个路径都是来自于其上方和左方
        #现将最上面的路径进行求和，最左边的路径进行求和
        for i in range(1,n):
            minLen.append(minLen[i-1] + grid[0][i])
        for i in range(1,m):
            for j in range(n):
                if j == 0:
                    minLen[j] += grid[i][0]
                else:
                    minLen[j] = min(minLen[j-1],minLen[j])+grid[i][j]
        return minLen[n-1]

    def minPathSum(self,grid):

        m = len(grid)
        n = len(grid[0])
        print(m,n)

        if m < 1 or n < 1:
            return 0

        minLen = [[0]*n for i in range(m)]
        minLen[0][0] = grid[0][0]

        # 计算第一行的值
        for i in range(1,n):
            minLen[0][i] = minLen[0][i-1] + grid[0][i]

        # 计算第一列的值
        for i in range(1,m):
            minLen[i][0] = minLen[i-1][0] + grid[i][0]

        # 计算其他的值
        # 只能从左边或者上面来 
        for i in range(1,m):
            for j in range(1,n):
                minLen[i][j] = min(minLen[i-1][j],minLen[i][j-1]) + grid[i][j]
        
        return minLen[m-1][n-1]

if __name__ == '__main__':

    s = Solution()
    grid = [[1,2,5],
            [3,2,1]]
    result = s.minPathSum(grid)
    print(result)
