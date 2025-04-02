import numpy as np

def format_strings(arr):
    """Format strings with padding, centering, left, and right justification."""
    formatted = {
        "centered": [f"{s:^15}" for s in arr],
        "left_justified": [f"{s:<15}" for s in arr],
        "right_justified": [f"{s:>15}" for s in arr]
    }
    return formatted

arr = np.array(["apple", "banana", "cherry", "date"])
formatted_arr = format_strings(arr)

print("Centered:\n", formatted_arr["centered"])
print("Left Justified:\n", formatted_arr["left_justified"])
print("Right Justified:\n", formatted_arr["right_justified"])
