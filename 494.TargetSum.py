#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 16:07:22 2017
@author: Sandra
"""

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        # 根据数学推导
        # (1) sum(P) - sum(N) = target
        # (2) sum(P) = (target + sumNums)/2
        n = len(nums)
        sumNums = sum(nums)
        sumP = (S + sumNums)/2
        sumN = sumP - S
        
        # 数组长度小于1 or 数组之和小于目标值 or sumP为奇数 返回0
        if n < 1 or sumNums < S:
            return 0
        
        print(sumP,sumN)
        
        # 初始化dp
        dp = [0]*(sumP+1)
        dp[0] = 1
        
        # 遍历
        for x in nums:
            # 判断 数组中是否有和为sumP的子数组
            for i in range(sumP,x-1,-1):
                dp[i] += dp[i-x]
        
        print(dp)           
        return dp[sumP]

if __name__ == '__main__':

    s = Solution()
    l = [1,1,1,1,1]
    S = 3
    result = s.findTargetSumWays(l,S)
    print(result)