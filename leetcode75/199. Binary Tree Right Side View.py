#199. Binary Tree Right Side View
#Medium
#problem statement:   https://leetcode.com/problems/binary-tree-right-side-view/description/?envType=study-plan-v2&envId=leetcode-75

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        q = collections.deque([root])
        res = []
        while q:
            res.append(q[-1].val)
            q_len = len(q)
            for i in range(q_len):
                left_most = q.popleft()
                if left_most.left: q.append(left_most.left)
                if left_most.right: q.append(left_most.right)
        return res


        #approach 2, dump the next level to an new list when moving to next level, this is a more intuitive way
