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
    # 二叉树的前序遍历
    # 根节点->左子树->右子树
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.Iterative(root)
    
    # 使用迭代的方式    
    def Recursive(self,root):
        # 声明堆栈
        travelStack = []
        # 声明存放结果的数组
        travelList = []
        # 设置当前节点为根节点
        curNode = root
        # 当前节点不是空节点 or 堆栈里有节点
        # 目的: 遍历二叉树
        while curNode != None or len(travelStack) > 0:
            # 当前节点不是空节点
            while curNode != None:
                # 添加该节点的值
                travelList.append(curNode.val)
                # 丢进堆栈
                travelStack.append(curNode)
                # 当前节点为节点的左孩子
                curNode = curNode.left
            # 堆栈POP
            curNode = travelStack.pop()            
            # 当前节点为节点的右孩子
            curNode = curNode.right
        return travelList 
    
    # 使用递归的方式 
    def Iterative(self,root):
        # 声明存放结果的数组
        travelList = []
        self.preOrder(travelList,root)
        return travelList
        
    def preOrder(self,travelList,node):
        if node != None:
            travelList.append(node.val)
            self.preOrder(travelList,node.left)
            self.preOrder(travelList,node.right)
        
if __name__ == "__main__":
    
    # test case
    root = TreeNode(1)
    subNode = TreeNode(2)
    subNode.left = TreeNode(3)
    root.right = subNode
    
    s = Solution()
    result = s.preorderTraversal(root)
    print(result)