from typing import List, Tuple

def is_prime(n: int) -> bool:
    """
    Check if a number is prime.
    
    Args:
        n (int): Number to check for primality
    
    Returns:
        bool: True if the number is prime, False otherwise
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_prime_path(grid: List[List[int]]) -> List[Tuple[int, int]]:
    """
    Find a continuous path of cells forming a prime number sequence.
    
    Args:
        grid (List[List[int]]): 2D grid of integers
    
    Returns:
        List[Tuple[int, int]]: List of cell coordinates forming a prime path,
                                or an empty list if no prime path exists
    
    Raises:
        ValueError: If grid is empty or None
    """
    # Input validation
    if not grid or not grid[0]:
        raise ValueError("Grid cannot be empty")
    
    rows, cols = len(grid), len(grid[0])
    
    def dfs(r: int, c: int, current_path: List[Tuple[int, int]], 
            visited: set) -> List[Tuple[int, int]]:
        """
        Depth-first search to find prime number path.
        
        Args:
            r (int): Current row
            c (int): Current column
            current_path (List[Tuple[int, int]]): Current path of coordinates
            visited (set): Set of visited coordinates
        
        Returns:
            List[Tuple[int, int]]: Prime path if found, else empty list
        """
        # Special case: single prime cell
        if len(grid) == 1 and len(grid[0]) == 1 and is_prime(grid[0][0]):
            return [(0, 0)]
        
        # Check if current cell forms a valid prime number
        current_number = int(''.join(str(grid[x][y]) for x, y in current_path))
        
        # If path is longer than 1 and prime, return the path
        if len(current_path) > 1 and is_prime(current_number):
            return current_path
        
        # If path is not yet prime or too short, continue searching
        if not is_prime(current_number):
            return []
        
        # Possible move directions: up, right, down, left
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        for dr, dc in directions:
            new_r, new_c = r + dr, c + dc
            
            # Check if new position is valid
            if (0 <= new_r < rows and 0 <= new_c < cols and 
                (new_r, new_c) not in visited):
                
                new_path = current_path + [(new_r, new_c)]
                new_visited = visited.copy()
                new_visited.add((new_r, new_c))
                
                # Recursive search
                result = dfs(new_r, new_c, new_path, new_visited)
                if result:
                    return result
        
        return []
    
    # Try starting the path from each cell
    for r in range(rows):
        for c in range(cols):
            path = dfs(r, c, [(r, c)], {(r, c)})
            if path:
                return path
    
    return []  # No prime path found