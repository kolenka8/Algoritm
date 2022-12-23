class Solution:
    def tribonacci(self, n: int) -> int:
        x1, x2, x3 = 0, 1, 1
        for _ in range(n):
            x1, x2, x3 = x2, x3, x1 + x2 + x3
        return x1