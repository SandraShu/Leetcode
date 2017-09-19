#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 10:25:17 2017

@author: Sandra
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 排序, 并筛选出小于target的值       
        sample = []
        for x in nums:
            sample.append(x)
            
        nums.sort()  
        
        if nums[0] > 0: 
            nums.append(target)
            #nums = list(set(nums))
            nums.sort()                    
            nums = nums[:nums.index(target)] 
        
        # 判断数组长度
        count = len(nums)
        if count < 1:
            return []
               
        # 左右游标
        left = 0
        right = count-1
        
        # 判断加法
        while left <= count/2 + 1:

            if nums[left] + nums[right] < target:
                left = left + 1
            elif nums[left] + nums[right] == target:
                
                result_left = sample.index(nums[left])
                result_right = sample.index(nums[right])
                
                if nums[left] == nums[right]:
                    result_right = sample[result_left+1:].index(nums[right])+result_left + 1
                                         
                return [result_left, result_right]
            
            elif nums[left] + nums[right] > target:
                right = right - 1
            
        return []
        
    

if __name__ == '__main__':
    
    given_nums = [0,4,3,0]
    target = 0
    
    s = Solution()
    result = s.twoSum(given_nums, target)
    print(result)
