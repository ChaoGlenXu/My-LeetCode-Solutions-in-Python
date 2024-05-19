# 238. Product of Array Except Self
#Medium
#problem statement: https://leetcode.com/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        maxLen = len(nums) - 1
        out = [None] * (maxLen+1)
        pre = []
        post = []
        

        pre_accu = 1
        for i in nums:
            pre_accu *= i
            pre.append(pre_accu)

        print(pre)

        post_accu = 1
        for j in reversed(nums):
            post_accu *= j
            post.append(post_accu)
        post.reverse()

        print(post)
        left = 1
        right = 1
       
        for idx, x in enumerate(nums):
            if idx == 0: out[0] = post[1]
            elif idx +1 > maxLen: out[idx] = pre[idx-1]
            else: out[idx] = pre[idx-1] * post[idx+1]
        
        return out

