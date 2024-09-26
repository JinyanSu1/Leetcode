# link: https://leetcode.com/problems/reverse-nodes-in-k-group/



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        def getKth(head, k):
            while head and k-1:
                head = head.next
                k = k -1
            return head
        Prevhead = dummy
        while True:
            prev, cur = None, Prevhead.next
            for i in range(k):
                tempNode = cur.next
                cur.next = prev
                prev, cur = cur, tempNode
            Prevhead.next.next = cur
            
            NewPrevhead =Prevhead.next
            Prevhead.next = prev
            Prevhead = NewPrevhead
            if not getKth(cur, k):
                break
            
        return dummy.next


