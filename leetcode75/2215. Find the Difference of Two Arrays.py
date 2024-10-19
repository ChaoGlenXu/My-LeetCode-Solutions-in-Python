#2215. Find the Difference of Two Arrays
#Easy
#problem statement:  https://leetcode.com/problems/find-the-difference-of-two-arrays/description/?envType=study-plan-v2&envId=leetcode-75
# My code beats 99.88% in runtime

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        ans = [[None],[None]]
        set1 = set(nums1)
        set2 = set(nums2)

        ans[0], ans[1] = list(set1 - set2), list(set2 - set1)
        ''' 
        #alternatively, intuitive approach 
        instersection = set1 & set2
        ans[0] = list(set1 - instersection)
        ans[1] = list(set2 - instersection)
        '''
        return ans
        
