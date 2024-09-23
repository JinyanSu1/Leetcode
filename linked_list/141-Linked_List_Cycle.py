# link: https://leetcode.com/problems/linked-list-cycle/
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        if fast is None or fast.next is None:
            return False
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False
