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
    # 二叉树的后序遍历
    # 左子树->右子树->根节点
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.Recursive(root)
    
    # 使用递归的方式 
    def Iterative(self,root):
        # 声明存放结果的数组
        travelList = []
        self.postOrder(travelList,root)
        return travelList
        
    def postOrder(self,travelList,node):
        if node != None:           
            self.postOrder(travelList,node.left)
            self.postOrder(travelList,node.right)
            travelList.append(node.val)
        
if __name__ == "__main__":
    
    # test case
    root = TreeNode(1)
    subNode = TreeNode(2)
    subNode.left = TreeNode(3)
    root.right = subNode
    
    s = Solution()
    result = s.postorderTraversal(root)
    print(result)