def place_queens(n: int) -> list[list[int]]:
    # Helper function to check if a queen can be placed at row r and column c
    def is_valid(board: list[int], r: int, c: int) -> bool:
        # Check if there is a queen in the same column or diagonal
        for i in range(r):
            if board[i] == c or abs(i - r) == abs(board[i] - c):
                return False
        return True
    
    # Recursive function to find all valid ways of placing queens on the board
    def backtrack(board: list[int], r: int) -> None:
        if r == n:
            # All queens have been placed, add the board configuration to the result
            result.append(board[:])
            return
        
        # Try all possible columns for the queen in this row
        for c in range(n):
            if is_valid(board, r, c):
                board[r] = c
                backtrack(board, r+1)
                board[r] = -1
    
    result = []
    board = [-1] * n
    backtrack(board, 0)
    return result
