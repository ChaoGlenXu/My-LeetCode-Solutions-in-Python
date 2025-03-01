#88. Merge Sorted Array
#Easy
#problem statement:   https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        cur, m, n = m + n - 1, m - 1, n - 1 

        while  m >= 0 and n >= 0:
            if nums1[m] >= nums2[n]:
                nums1[cur] =  nums1[m]
                m -= 1
            else:
                nums1[cur] = nums2[n]
                n -= 1
            cur -= 1
        
        if m < 0:
            for i in range(n+1): nums1[i] = nums2[i]


        ''' #over complicated wrong
        if n == 0: return
        if m == 0: nums1[0] = nums2[0]
        p1, p2, p = m-1, n-1, m+n-1


        for i in range(p, -1, -1):
            if p1 < 0 or p2 < 0: break
            print("p1:  " + str(p1) + " p2: " + str(p2))
            if nums1[p1] >= nums2[p2]:
                nums1[i] = nums1[p1]
                p1 -= 1
                #p1 = 0 if p1-1 < 0 else p1-1
            else:
                nums1[i] = nums2[p2]
                p2 -= 1
                #p2 = 0 if p2-1 < 0 else p2-1
        nums1[0] = min(nums1[0], nums2[0])
        print(nums1)
        '''


        ''' #used sort(), may be required to solve it without using sort()
        for i in range(n): 
            nums1[m+i] = nums2[i]
        nums1.sort()
        '''
