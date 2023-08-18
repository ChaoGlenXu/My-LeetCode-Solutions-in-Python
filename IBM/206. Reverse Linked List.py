#206. Reverse Linked List
#Easy 
#problem statement:  https://leetcode.com/problems/reverse-linked-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        cur = head
        prev = None 
    
        while cur != None:
            nextNode = cur.next
            cur.next = prev
            
            prev = cur
            cur = nextNode
            
        return prev
