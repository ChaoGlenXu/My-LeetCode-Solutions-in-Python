class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dic = {}
        for idx, i in enumerate(nums):
            needed = target - i
            if needed in dic:
                return [dic.get(needed), idx]
            else:
                dic[i] = idx

