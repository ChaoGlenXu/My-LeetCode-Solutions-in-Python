#1448. Count Good Nodes in Binary Tree
#Medium
#problem statement:   https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #recursive approach
        count = 0

        def dfs(r, cur_max):
            nonlocal count
            if r == None: return 
            if r.val >= cur_max:
                cur_max = r.val
                count += 1
            return dfs(r.left, cur_max), dfs(r.right, cur_max)

        dfs(root, root.val)
        return count 
