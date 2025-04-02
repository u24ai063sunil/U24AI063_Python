import numpy as np

def generate_magic_square(n):
    """Generate an odd-order magic square using the Siamese method."""
    if n % 2 == 0:
        raise ValueError("Only odd N is supported for this method.")
    
    magic_square = np.zeros((n, n), dtype=int)
    num = 1
    i, j = 0, n // 2

    while num <= n * n:
        magic_square[i, j] = num
        num += 1
        ni, nj = (i - 1) % n, (j + 1) % n
        if magic_square[ni, nj]:
            i += 1
        else:
            i, j = ni, nj
    return magic_square

N = 5  # Change to 4, 6, 7, 8 as needed
print(generate_magic_square(N))
