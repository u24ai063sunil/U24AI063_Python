import pandas as pd
s = pd.Series(['X', 'Y', 'T', 'Aaba', 'Baca', 'CABA', None, 'bird', 'horse', 'dog'])

# Convert to upper
upper = s.str.upper()

# Convert to lower
lower = s.str.lower()

# String length
length = s.str.len()

print("Upper:\n", upper)
print("Lower:\n", lower)
print("Length:\n", length)
