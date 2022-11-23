def rob(nums: list[int]) -> int:
    """Сложность данной функции O(n).
        nums (List[int]): сумма денег в каждом доме
    Returns:
        int: максимальная сумму денег, которую мы можем украсть.
    """ 
    def helper(nums):
        dp1, dp2 = 0, 0
        for num in nums:
            dp1, dp2 = dp2, max(dp1 + num, dp2)          
        return dp2
    return max(nums[0] + helper(nums[2:-1]), helper(nums[1:]))