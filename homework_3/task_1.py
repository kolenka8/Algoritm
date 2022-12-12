from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: List) -> bool:
        """The complexity of this algorithm O(1).
        Args:
                List: the number of nodes in the list
        Returns:
                bool: is the list of number a palindrome
        """
        if not head or not head.next:
            return True
        head_2=head
        reverse=self.reverse_list(head_2)
        while head!=None:
            if head.val!=reverse.val:
                return False
            reverse=reverse.next
            head=head.next
        return True
    def reverse_list(self,head) -> List:
        cur=head
        reverse=None
        while cur:
            temp=cur.next
            cur.next=reverse
            reverse=cur
            cur=temp
        return reverse