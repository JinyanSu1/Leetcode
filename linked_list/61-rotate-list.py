# link: https://leetcode.com/problems/rotate-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        cur =  head
        while cur:
            cur = cur.next
            count += 1
        
        if count == 0:
            return head
        num_move = k % count
        if num_move ==0:
            return head
        slow, fast = head, head
        for i in range(num_move):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        New_head = slow.next
        slow.next =None
        fast.next = head
    
        return New_head
        