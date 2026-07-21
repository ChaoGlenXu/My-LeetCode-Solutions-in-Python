#4. Median of Two Sorted Arrays
#Hard
#problem statement:    https://leetcode.com/problems/median-of-two-sorted-arrays/description/?envType=problem-list-v2&envId=plakya4j

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2

        a, b = nums1, nums2
        if len(b) < len(a): a, b = b, a  # a is always the smaller one

        l, r = 0, len(a) - 1
        while (True):
            m_a = (r + l) // 2
            m_b = half - m_a - 2

            a_left = a[m_a] if m_a >= 0 else float("-inf")
            a_right = a[m_a + 1] if m_a + 1 < len(a) else float("inf")
            b_left = b[m_b] if m_b >= 0 else float("-inf")
            b_right = b[m_b + 1] if m_b + 1 < len(b) else float("inf")

            if a_left <= b_right and b_left <= a_right:
                if total % 2:
                    return min(a_right, b_right)
                else:
                    return (max(a_left, b_left) + min(a_right, b_right))/2

            else:
                if a_left > b_right:
                    r = m_a - 1
                elif b_left > a_right:
                    l = m_a + 1

                
