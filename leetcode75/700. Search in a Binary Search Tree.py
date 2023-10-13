#700. Search in a Binary Search Tree
#Easy
#problem statement: https://leetcode.com/problems/search-in-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def fun(node, val):  
            if node == None:
                return None
            print(node.val)
            if node.val == val:
                return node
            #elif node.left == None and node.right == None:
            #    return None
            elif val < node.val:
                return fun(node.left, val)
            else:
                return fun(node.right, val)
        
        return fun(root, val)
