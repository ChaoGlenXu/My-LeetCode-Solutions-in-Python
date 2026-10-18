#303. Range Sum Query - Immutable
#Easy
#problem statement:    https://leetcode.com/problems/range-sum-query-immutable/description/

class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        res = 0
        for i in range(left, right+1):
            res += self.nums[i]
            #print(i)
        #print("done")
        return res


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
