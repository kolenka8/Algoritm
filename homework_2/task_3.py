from typing import List

def uniq_paths_with_obstacles(grid: List[List[int]]) -> int:
    """Сложность данной функции O(n**2)
    Args:
        grid (List[List[int]]): сетка, которую мы должны исследовать.
    Returns:
        int: Количество возможных уникальных путей, по которым робот может добраться до нижнего правого угла.
    """                    
    matrix = [[1] * len(grid) for _ in range(len(grid))]
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix)):
            if grid[i][j] + grid[i-1][j] + grid[i][j-1] == 0:
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
            elif grid[i][j-1] + grid[i-1][j] == 2 or grid[i][j] == 1:
                matrix[i][j] = 0
            elif grid[i-1][j] == 1:
                matrix[i][j] = matrix[i][j-1]
            elif grid[i][j-1] == 1:
                matrix[i][j] = matrix[i-1][j]         
    return matrix[-1][-1]