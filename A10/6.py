import numpy as np
import matplotlib.pyplot as plt

def f(x):
    """Define the polynomial function."""
    return x**3 - 4*x - 9

def bisection_method(a, b, tol=1e-5):
    """Find root using bisection method."""
    if f(a) * f(b) >= 0:
        raise ValueError("Invalid interval: f(a) and f(b) must have opposite signs.")
    
    iterations = []
    while (b - a) / 2 > tol:
        mid = (a + b) / 2
        iterations.append(mid)
        if f(mid) == 0:
            return mid, iterations
        elif f(a) * f(mid) < 0:
            b = mid
        else:
            a = mid
    return (a + b) / 2, iterations

root, steps = bisection_method(-5, 5)
steps = np.array(steps)

plt.plot(range(len(steps)), steps, marker='o', linestyle='-')
plt.xlabel("Iteration")
plt.ylabel("Root Approximation")
plt.title("Bisection Method Root Finding")
plt.grid()
plt.show()

print("Root found at:", root)
