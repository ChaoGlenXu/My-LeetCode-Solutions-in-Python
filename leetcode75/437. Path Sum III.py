#437. Path Sum III
#Medium
#problem statement:   https://leetcode.com/problems/path-sum-iii/description/?envType=study-plan-v2&envId=leetcode-75

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
    #what if two path next to each other continous: target sum -> target sum? then does this make it another path? yes, it does
        self.res = 0
        freq = {0:1}

        def dfs(r, pre):
            if not r:
                return 
            cs = pre + r.val
            x = cs - targetSum 
            if x in freq: self.res += freq[x]
            if cs not in freq: freq[cs] = 1 
            else: freq[cs] += 1 
            dfs(r.left, cs)
            dfs(r.right, cs) 
            freq[cs] -= 1

        dfs(root, 0)
        return  self.res
      
