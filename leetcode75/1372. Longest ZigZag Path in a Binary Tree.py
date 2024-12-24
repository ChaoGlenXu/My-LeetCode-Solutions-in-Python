#1372. Longest ZigZag Path in a Binary Tree
#Medium
#problem statement:   https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        self.res = 0

        def dfs(node, c, pre):
            if not node: return
            if pre == "None":
                dfs(node.left, 0, "left")
                dfs(node.right, 0, "right")
                return

            c += 1
            if c > self.res: self.res = c
            if pre == "left" and node.left: dfs(node.left, 0, "left")
            if pre == "left" and node.right: dfs(node.right, c, "right")
            if pre == "right" and node.left: dfs(node.left, c, "left")
            if pre == "right" and node.right: dfs(node.right, 0, "right")
        
        dfs(root, 0, "None")

        return self.res
