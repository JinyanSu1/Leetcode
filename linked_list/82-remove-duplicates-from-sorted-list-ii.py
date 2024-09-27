# link: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-101, head)
        prev, cur = dummy, head
        while cur and cur.next:
            if prev.next.val == cur.next.val:
                cur = cur.next
            else:
                prev, cur = cur, cur.next
            if prev.next!= cur:
                if (cur.next and prev.next.val != cur.next.val and prev.next.val == cur.val) or not cur.next:
                    prev.next = cur.next
                    cur = cur.next
        return dummy.next
