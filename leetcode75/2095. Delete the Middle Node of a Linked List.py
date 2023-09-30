# 2095. Delete the Middle Node of a Linked List
#Medium 
#problem statement: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #decide the #
        n = 1
        cur = head
        while cur.next != None:
            cur = cur.next
            n += 1

        mid = 0
        if n%2 == 1:
            mid = floor(n/2)
        else:
            mid = n/2
        
        print(mid)
        mid = int(mid)
        de = head

        def deleteNext(node):
            the = node.next
            afterThe = node.next.next
            the.val = None
            node.next = afterThe

        for i in range(mid + 1):
            if i == mid-1:
                deleteNext(de)
                return head
            de = de.next
            
        '''
        #decide the #
        n = len(head)
        mid = 0
        if n%2 == 1:
            mid = floor(n/2)
        else:
            mid = n/2
        
        res = head.copy()
        res.pop(mid)
        return res
        '''
        
