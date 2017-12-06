#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 10:07:39 2017

@author: Sandra
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        # 声明存放结果的数组
        travelList = []
        self.levelOrderFunction(travelList,root)
        return travelList

    def levelOrderFunction(self,travelList,node):
        if node != None:  
            travelList.append([node.val,depth])
            self.levelOrderFunction(travelList,node.left)
            self.levelOrderFunction(travelList,node.right)            
        
if __name__ == "__main__":
    
    # test case
    root = TreeNode(2)
    root.left = TreeNode(4)
    root.right = TreeNode(3)
    
    s = Solution()
    result = s.levelOrder(root)
    print(result)