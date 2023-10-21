# 1161. Maximum Level Sum of a Binary Tree
#Medium
#problem statement: https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        self.dic = {}

        def dfs(node, level):
            if not node:
                return
                
            if level not in self.dic:
               self.dic[level] = node.val 
            else:
                self.dic[level] += node.val 

            dfs(node.left, level+1)
            dfs(node.right, level+1)
            
        dfs(root, 1)

        maxV = max(self.dic.values())
        print(maxV)
        print(self.dic)
        for  i in self.dic:
            print(i)
            #print(idx, i)
            if self.dic[i] == maxV:
                return i
        
            
            




