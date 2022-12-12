from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """The complexity of this algorithm O(1).
        Args:
                Optional[TreeNode]: linked list with cycle
        Returns:
                bool: is a cycle in the linked list.
        """
        pt1, pt2 = head, head
        while pt2.next and pt2.next.next:
            pt2 = pt2.next.next
            pt1 = pt1.next
            if pt2 == pt1:
                return True      
        return False