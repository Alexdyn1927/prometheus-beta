from typing import List, Tuple

class BallStackSorter:
    """
    A class to sort three stacks of colored balls with specific constraints.
    
    Constraints:
    - Only move one ball at a time
    - Maintain equal number of balls in each stack
    - Colors: Red, Blue, Green
    """
    
    def __init__(self, stacks: List[List[str]]):
        """
        Initialize the ball stack sorter with three stacks of colored balls.
        
        :param stacks: A list of three lists representing the initial ball stacks
        :raises ValueError: If initial conditions are not met
        """
        if len(stacks) != 3:
            raise ValueError("Must provide exactly 3 stacks")
        
        # Validate that all stacks have the same number of balls
        if len(set(len(stack) for stack in stacks)) != 1:
            raise ValueError("All stacks must have equal number of balls")
        
        # Validate balls are only Red, Blue, or Green
        valid_colors = {'Red', 'Blue', 'Green'}
        for stack in stacks:
            if not all(ball in valid_colors for ball in stack):
                raise ValueError("Balls must be Red, Blue, or Green")
        
        self.stacks = [stack.copy() for stack in stacks]
        self.moves = []
    
    def sort(self) -> List[List[str]]:
        """
        Sort the stacks of balls.
        
        :return: Sorted stacks of balls
        """
        while not self.is_sorted():
            # Find the optimal move
            move = self._find_best_move()
            if move is None:
                raise ValueError("Unable to sort stacks")
            
            # Execute the move
            from_stack, to_stack = move
            ball = self.stacks[from_stack].pop()
            self.stacks[to_stack].append(ball)
            self.moves.append((from_stack, to_stack))
        
        return self.stacks
    
    def _find_best_move(self) -> Tuple[int, int]:
        """
        Find the best move to progress towards sorting.
        
        :return: A tuple of (from_stack, to_stack) indices
        """
        # Analyze color distributions
        for i in range(3):
            for j in range(3):
                if i != j and self._is_valid_move(i, j):
                    return i, j
        
        return None
    
    def _is_valid_move(self, from_stack: int, to_stack: int) -> bool:
        """
        Check if moving a ball from one stack to another is valid.
        
        :param from_stack: Index of source stack
        :param to_stack: Index of destination stack
        :return: Whether the move is valid
        """
        if not self.stacks[from_stack]:
            return False
        
        return True
    
    def is_sorted(self) -> bool:
        """
        Check if all stacks have the same colors.
        
        :return: True if stacks are sorted, False otherwise
        """
        # If stacks are empty, consider them sorted
        if not any(self.stacks):
            return True
        
        # Check if each stack has the same color
        return all(
            len(set(stack)) <= 1 
            for stack in self.stacks
        )
    
    def get_moves(self) -> List[Tuple[int, int]]:
        """
        Get the list of moves made during sorting.
        
        :return: List of moves as (from_stack, to_stack) tuples
        """
        return self.moves.copy()