# 236. Lowest Common Ancestor of a Binary Tree
#Medium
#problem statement: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None

        def dfs(node):
            if not node:
            #if node == None:
                return False
            left = dfs(node.left)
            right = dfs(node.right)
            cur = node == q or node == p

            if (left and right) or (left and cur) or (right and cur):
                self.ans = node
                return 
            return left or right or cur
        dfs(root)
        return self.ans


        '''
        #def dfs(node ):
        cur = root

        while cur:
            
            if (q.val <= cur.val and p.val >= cur.val) or (q.val >= cur.val and p.val <= cur.val):
                return cur
            elif (q.val < cur.val and p.val < cur.val):
                cur = cur.left
            else:
                cur = cur.right
        '''
        '''
            if (q.val < cur.val and p.val < cur.val):
                cur = cur.left
            elif(q.val > cur.val and p.val > cur.val):
                cur = cur.right
            else:
                return cur
        '''
