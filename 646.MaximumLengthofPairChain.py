#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 16:07:22 2017
@author: Sandra
"""

class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        # 数组长度
        n = len(pairs)
        # 长度小于2 返回0
        if n < 2:
            return 0
        # 按照pair[1]排序
        pairs = sorted(pairs,key=lambda x: x[1])
        print(pairs)
        # 遍历
        pos,length = 0,0
        while pos < n:
            # pos
            temp = pos
            # 对pos之后的数据做比较
            for i in range(pos,n):
                # 判断
                if pairs[i][0] > pairs[pos][1]:
                    # pos更新位置
                    pos = i
                    # length自增1
                    length += 1
                    # 结束本次循环
                    break
            # 如果此次的遍历 pos的位置没有更新
            # 即没有符合要求的数组出现 
            # 退出
            if pos == temp:
                break
        return length+1

if __name__ == '__main__':

    s = Solution()
    l = [[-1,1],[-2,7],[-5,8],[-3,8],[1,3],[-2,9],[-5,2]]
    result = s.findLongestChain(l)
    print(result)