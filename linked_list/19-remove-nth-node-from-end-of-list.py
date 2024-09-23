# link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow, fast = head, head
        new_node = slow
        count = 0
        flag = False
        while count < n:
            fast = fast.next
            count += 1
        while fast:
            fast = fast.next
            new_node = slow
            slow = slow.next
            flag = True
        if not flag and not slow.next:
            return None
        if not slow.next:
            new_node.next = None
        else:
            slow.val = slow.next.val
            slow.next = slow.next.next
        
        return head

