# link: https://leetcode.com/problems/copy-list-with-random-pointer/
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        Nodemap = {}
        cur = head
        while cur:
            Nodemap[cur] = Node(cur.val)
            cur = cur.next
        Nodemap[None] = None
        cur = head
        while cur:
            Nodemap[cur].next = Nodemap[cur.next]
            Nodemap[cur].random = Nodemap[cur.random]
            cur = cur.next
        return Nodemap[head]

