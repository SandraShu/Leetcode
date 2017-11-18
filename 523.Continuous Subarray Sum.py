#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 16:59:22 2017
@author: Sandra
"""

class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 数组长度
        n = len(nums)
        # 如果和为零 或 数组长度小于2 返回 False
        if (k == 0 and sum(nums) != 0) or n < 2:
            return False
        # 如果和为零 并且数组元素都为0  返回 True
        if k == 0 and sum(nums) == 0:
            return True
        # 遍历
        for i in range(n-1):
            # init dp
            dp = [0]*(n-i)
            dp[0] = nums[i]
            # 遍历下一位
            for j in range(i,n):
                # 求和
                dp[j-i] = dp[j-i-1] + nums[j]
                # 判断子数组之和是否为k的倍数
                if dp[j-i] % k == 0 and j != i:
                    #print(i,j,dp[j-i])
                    return True
        return False
if __name__ == '__main__':

    s = Solution()
    l = [5,2,4]
    k = 5
    result = s.checkSubarraySum(l, k)
    print(result)