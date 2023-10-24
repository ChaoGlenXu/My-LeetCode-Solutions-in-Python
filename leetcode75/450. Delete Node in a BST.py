#450. Delete Node in a BST
#Medium 
#problem statement: https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            cur = root.right
            while(cur.left):
                cur = cur.left
            root.val = cur.val

            #delete the node of the leftist most child of the right hand side of the subtree for the found node
            root.right = self.deleteNode(root.right, root.val)
        
        return root
        '''
        def dfs(node):
            if not node:
                return False
            
            if node.val == key:
                re
        '''
