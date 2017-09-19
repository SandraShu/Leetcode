#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 11:27:37 2017

@author: Sandra
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        '''
        遍历该字符串，每遍历一个字母时，找该字母最近一次出现是什么时候
        中间这一段便是无重复字符的字符串
        
        
        pos = 0
        dic = {}
        
        for x in s:
            
            if x not in dic:
                dic[x] = [pos]
                pos = pos + 1
                continue
            
            dic[x].append(pos)
            pos = pos + 1
        '''
        

        # 滑窗
        i=0
        j=0
        length=0
        target = ''
        num = len(s)
        
        while i<num and j<num:
            if s[j] not in target:               
                target = target + s[j]
                j = j+1
                length = j-i>length and j-i or length
                print('y',j,target)
            else:                
                target = target[1:]
                i = i+1
                print('n',i,target)
            
        return length
                     
if __name__ == '__main__':
    
    string = "dssldlzuzvelfddoyrvzggneabubhnnkigwntxjuvnfaskpsdkumshqsikwrzjchrawkxfesumv"
       
    s = Solution()
    result = s.lengthOfLongestSubstring(string)
    print(result)