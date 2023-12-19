#203. Remove Linked List Elements
#Easy
#problem statement:   https://leetcode.com/problems/remove-linked-list-elements/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        if head == None: return head
        if head.next == None and head.val == val: return None
        start = head
        while start.val == val:
            start = start.next
            if start.next == None:
                if start.val == val:
                    return None
                return start

        prev = start
        cur = start
        
        while cur.next != None:
            if cur.val == val:
                prev.next = cur.next
                cur = cur.next
            else:
                prev = cur
                cur = cur.next

        if cur.val == val:
            prev.next= None

        return start
        
