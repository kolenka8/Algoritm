from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    """The complexity of this algorithm O(1).
        Args:
                List: reference node to a singly-linked list.
        Returns:
                int: Return the decimal value of the number in the linked list.
    """
    def getDecimalValue(self, head: List) -> int:    
        res = ''
        while head:
            res = res+str(head.val)
            head = head.next
        print(res)
        return int(res,2)