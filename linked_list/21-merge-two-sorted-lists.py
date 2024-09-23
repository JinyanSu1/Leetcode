# link: https://leetcode.com/problems/merge-two-sorted-lists/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        merged_list = ListNode(0)
        current_list = merged_list
        
        current1, current2 = list1, list2
        while current1 and current2:
            if current1.val <= current2.val:
                current_list.next = ListNode(current1.val)
                current_list = current_list.next
                current1 = current1.next
            else:
                current_list.next = ListNode(current2.val)
                current_list = current_list.next
                current2 = current2.next
        if current1:
            current_list.next = current1
        else:
            current_list.next = current2
        return merged_list.next

