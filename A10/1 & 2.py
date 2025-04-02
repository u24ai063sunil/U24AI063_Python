from itertools import permutations

def is_valid(board):
    """Check if the board configuration is valid (no queens attacking each other)."""
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if abs(board[i] - board[j]) == abs(i - j):  # Diagonal check
                return False
    return True

def solve_n_queens(n=8):
    """Solve the N-Queens problem and return all solutions."""
    solutions = []
    for perm in permutations(range(n)):
        if is_valid(perm):
            solutions.append(perm)
    return solutions

solutions = solve_n_queens()
print(f"Total solutions found: {len(solutions)}")
for sol in solutions[:5]:  # Print first 5 solutions
    print(sol)
