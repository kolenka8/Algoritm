from typing import List

def max_profit(values: (List[int])) -> int:
    """Сложность данной функции O(n).
    Args:
        values (List[int]): целочисленный массив значений
    Returns:
        int: максимальная прибыль
    """        
    return sum(max(values[i] - values[i-1], 0) for i in range(1, len(values)))