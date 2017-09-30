#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 20:37:52 2017

@author: Sandra
"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        num = len(s)
        
        # 只有一列或者字符串长度小于2
        if numRows == 1 or num < 2:
            return s
        
        # 两列以上      
        numCols=num/2 + 1  
        pos,matrix = 0,[]
        
        # 初始化矩阵
        for i in range(numRows):
            matrix.append([])            
            for j in range(numCols):                               
                matrix[i].append([])
                matrix[i][j] = '-'     
        
        # z型填充矩阵
        for j in range(numCols):
            for i in range(numRows):
                if (j%(numRows-1)  == 0 or (j+i)%(numRows-1) == 0) and pos<num:
                    matrix[i][j] = s[pos]
                    pos = pos+1
        
        # 拼接变形后的字符串
        result = ''
        for row in matrix:
            print(row)
            for i in row:
                if i != '-':
                    result = result+i      
        
        return result
            
if __name__ == '__main__':
      
    ss = 'yjvsbxetkierlqfbxyetjbyqqgrtrurpfmkhjocwyjpjzunxsrqdurtkxngqjxgokqxvgarejgqkadhuuayortbqgjhpgpgsfdolffrqmhbokklgklxdeywnhfepukibqwoxbfqpnrgzdrgocdtidpxmucbqojrghfelnuaangzszhibmcmptjbqnfgcoykyfojskluzuwstdaxqejhyuloiqumguwecnnuzbpzvntoqvliawsatdobtkpzhlejytfauwzrjugcptmrserlhhoaudcboimpdrpaqqrzmxddtqvluoweymgspitfshwwynwqfnqrnvvilstiirmgduyuftzxawvbjrrphjiwffgszzcisqoxlprqkqnloloaehrltzjahpsgqxoknfhywyogrethphhtrahkcsmjkgpcdgnrnwpjxgpqkjxbshwlhfxjyjskqkmtqbkdycovidnuokvjrtubzukzdfjtpxphzzmzbawlfjfuvcfpwbqxvcyzhhuygjhhltgoteaznhvlkaaidqhzsfacoucwekerfmfzrhagpxrbxtlajsbezbgnwklcupvaeabviddxaxazqlbcddgcgoreacixudzyeavofanfxngqyhubmaftqyzqcinylowrotfvusctfijdsdggfnbxnbqsjfqwupokitgcmiwtthxlnfruvtsiuiafprbjgpuq'
    n = 415
       
    s = Solution()
    result = s.convert(ss,n)
    print(result)