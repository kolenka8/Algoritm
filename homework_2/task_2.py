def get_max_generated(n: int) -> int:  
    """Сложность данной функции O(n)
    Args:
        n (int): длина списка.
    Returns:
        int: максимальный элемент в этом списке.
    """        
    nums = [0] * (n + 1)
    nums[1] = 1
    for i in range(1, len(nums) // 2):
        if 2 <= 2 * i <= n:
            nums[2 * i] = nums[i]
        if 2 <= 2 * i + 1 <= n:
            nums[2 * i + 1] = nums[i] + nums[i + 1]
    return max(nums)