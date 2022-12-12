from typing import List, Optional
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def averageOfLevels(self, root):
        """The complexity of this algorithm O(1).
        Args:
                Optional[TreeNode]: binary tree
        Returns:
                List[float]: return average value of the nodes on each level in the form of an array.
        """
        res = []
        stack = [root]
        while stack:
            res.append(sum([x.val for x in stack])/float(len(stack)))
            next_stack = []
            for x in stack:
                if x.left:
                    next_stack.append(x.left)
                if x.right:
                    next_stack.append(x.right)
            stack = next_stack
        return res