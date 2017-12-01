#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 10:07:39 2017

@author: Sandra
"""
import sys
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return True
        return self.isValidBSTFunction(root,-sys.maxsize,sys.maxsize)

    def isValidBSTFunction(self,node,minVal,maxVal):
        
        if node == None:           
            return True
        
        if node.val <= minVal or node.val >= maxVal:
            return False
        
        # 左子树 (minVal, node.val)
        # 右子树 (node.val, maxVal)
        return self.isValidBSTFunction(node.left, minVal, node.val) and self.isValidBSTFunction(node.right, node.val, maxVal)
        
if __name__ == "__main__":
    
    # test case
    root = TreeNode(2)
    root.left = TreeNode(4)
    root.right = TreeNode(3)
    
    s = Solution()
    result = s.isValidBST(root)
    print(result)