#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 08:29:22 2017

@author: Sandra
"""
import copy

class Solution(object):
    # 求四数之和
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # length of nums
        if len(nums) < 4:
            return []
        # four same number
        result = []
        for x in set(nums):
            if nums.count(x) > 3 and x*4 == target:
                result.append([x,x,x,x])
        # max or min
        nums.sort()
        if nums[len(nums)-1] + nums[len(nums)-2] + nums[len(nums)-3] + nums[len(nums)-4] < target or nums[0] + nums[1] + nums[2] + nums[3] > target:
            return []
        # first two sum
        fd = self.twoSum(nums)
        # second two sum
        sd = self.twoSum(fd.keys())
        # not exist target
        if target not in sd:
            return result
        # find target
        for x in sd[target]:
            for i in range(len(fd[x[0]])):
                for j in range(len(fd[x[1]])):
                    # four sum
                    temp = fd[x[0]][i] + fd[x[1]][j]
                    # sort
                    temp.sort()
                    # not contain duplicate quadruplets
                    if temp not in result:
                        # duplicate item
                        nums_t = copy.deepcopy(nums)
                        flag = True
                        for a in temp:
                            if a in nums_t:
                                nums_t.remove(a)
                            else:
                                flag = False
                                break
                        if flag == True:
                            result.append(temp)
        return result

    # 求两数之和
    def twoSum(self,nums):
        # 求两两之和
        d={}
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):       		
                if nums[i]+nums[j] not in d:
                    d[nums[i]+nums[j]] = []
                d[nums[i]+nums[j]].append([nums[i],nums[j]])
        # 返回两两求和的字典，key为和值，value为元素
        return d

if __name__ == '__main__':

    s = Solution()
    #l = [-493,-482,-482,-456,-427,-405,-392,-385,-351,-269,-259,-251,-235,-235,-202,-201,-194,-189,-187,-186,-180,-177,-175,-156,-150,-147,-140,-122,-112,-112,-105,-98,-49,-38,-35,-34,-18,20,52,53,57,76,124,126,128,132,142,147,157,180,207,227,274,296,311,334,336,337,339,349,354,363,372,378,383,413,431,471,474,481,492]
    #l=[-7,-5,0,7,1,1,-10,-2,7,7,-2,-6,0,-10,-5,7,-8,5]
    l=[-497,-494,-484,-477,-453,-453,-444,-442,-428,-420,-401,-393,-392,-381,-357,-357,-327,-323,-306,-285,-284,-263,-262,-254,-243,-234,-208,-170,-166,-162,-158,-136,-133,-130,-119,-114,-101,-100,-86,-66,-65,-6,1,3,4,11,69,77,78,107,108,108,121,123,136,137,151,153,155,166,170,175,179,211,230,251,255,266,288,306,308,310,314,321,322,331,333,334,347,349,356,357,360,361,361,367,375,378,387,387,408,414,421,435,439,440,441,470,492]
    result = s.fourSum(l,1682)
    print(result)
