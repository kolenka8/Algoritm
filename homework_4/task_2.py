class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root) -> int:
        if root is None:
            return 0
        stack = [(root, 0)]
        max_depth = float('inf')
        while stack:
            curr, depth = stack.pop()

            if curr.left is not None:
                stack.append((curr.left, depth + 1))

            if curr.right is not None:
                stack.append((curr.right, depth + 1))

            if (curr.right and curr.left) is None:
                    if depth < max_depth:
                        max_depth = depth
        return max_depth