#2130. Maximum Twin Sum of a Linked List
#Medium
#problem statement:   https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/?envType=study-plan-v2&envId=leetcode-75

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        res, li, cur = 0, [], head
        #print(head)
        li.append(head.val)

        while cur.next != None:
            cur = cur.next
            li.append(cur.val)

        size = len(li)
        #print(size)
        for i in range(int(size/2)):
            #print(str(i) + "  " + str(li[i]) + " + " + str(li[-i-1]))
            twin_sum = (li[i] + li[-i-1])
            if twin_sum > res:
                res = twin_sum 
     
        return res
