from types import List

def get_descent_periods(values: List[int]) -> int:
    """Сложность данной функции O(n)
    Args:
        values (List[int]): целочисленный массив значений
    Returns:
        int: количество периодов плавного спуска
    """        
    lst = [1] * len(values)
    for i in range(1, len(lst)):
        if values[i] - values[i-1] == -1:
            lst[i] += lst[i-1] 
    return sum(lst)