# 104. Maximum Depth of Binary Tree
#Easy
#problem statement: https://leetcode.com/problems/maximum-depth-of-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        #recursive DFS
        #depth = 0
        cur = root
        def dfs( cur):
            if cur == None:
                return 0
            if cur.left == None and cur.right == None:
                return 1
            else:
                return 1 + max(dfs(cur.left), dfs(cur.right))

        return dfs(cur)
