#88. Merge Sorted Array
#Easy 
#problem statement:  https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        #passed all test cases, used accumulated 26 mins to code 
        count = 0
        for i in range(m, len(nums1)):
            nums1[i] = nums2[count]
            count += 1

        nums1.sort()



        '''
        #passed 58/59 test cased. used accumulated 20 mins to code
        l1 = m
        l2 = n
        new = []
        cur = l1 -1
        while cur >= 1 and nums1[cur] == 0:
            cur -= 1

        print(cur)
        for i in range(0, cur+1):
            new.append(nums1[i])
        
        cur = l2 - 1
        #print(nums2[cur])
        while cur >= 1 and nums2[cur] == 0:
            cur -= 1

        for i in range(0, cur+1):
            new.append(nums2[i])

        
        nums1.clear()
        nums1.extend(new)

        #nums1.extend(nums2)
        nums1.sort()
        '''

        '''
        #pased half test cases, used 10 minutes
        start1 = l1 -1
        for idx, i in enumerate(list(reversed(nums1))):
            if i == 0:
                #new.append(i)
            else:
                start1 -= 1
        '''   
        '''     
        flip = False

        for i in nums1:
            if i > 0:
        '''
