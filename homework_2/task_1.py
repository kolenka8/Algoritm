from typing import List

def count_squares(matrix: List[List[int]]) -> int:
    """Сложность данного алгоритма O(n**2).
    Args:
        matrix (List[List[int]]): матрица, в которой мы ищем квадраты.
    Returns:
        int: количество квадратов в матрице.
    """
    cp_matr = [row for row in matrix]
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j]:           
                cp_matr[i][j] = 1 + min(cp_matr[i][j-1], cp_matr[i-1][j-1], cp_matr[i-1][j])
    return sum([sum(i) for i in cp_matr])