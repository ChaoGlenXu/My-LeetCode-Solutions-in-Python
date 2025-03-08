#238. Product of Array Except Self
#Medium
#problem statement:   https://leetcode.com/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res, prefix, postfix = [1] * len(nums), 1, 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res
        
        
        ''' #wrong
        res, prefix, postfix = [], [nums[0]], [nums[-1]]

        for idx, i in enumerate(nums[1:], start=1):
            prefix[idx] = i * prefix[idx-1]

        for i in range(len(nums)-2, -1, -1):
            postfix.insert(0, i * [prefix[0]])
        
        res = [postfix[1]]
        for i in range(1, len(nums)-1):
            res[i] = prefix[i-1] * postfix[i+1]
        res.append(prefix[-2])

        return res
        '''
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        '''
        #durring the leetcode 75
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
        '''
