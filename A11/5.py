import numpy as np
from itertools import product
import pandas as pd

# Sample dataset
concerts = pd.DataFrame({
    'artist': ['A', 'B', 'A', 'C', 'B'],
    'venue': ['X', 'Y', 'X', 'Z', 'Y'],
    'date': pd.to_datetime(['2023-01-15', '2023-01-20', '2023-02-01', '2023-01-30', '2023-02-20'])
})

# Add year-month column
concerts['year_month'] = concerts['date'].dt.to_period('M')

# Group by year_month, artist, venue
grouped = concerts.groupby(['year_month', 'artist', 'venue']).size().unstack(fill_value=0)

# Get all artist-venue combinations
artists = concerts['artist'].unique()
venues = concerts['venue'].unique()
all_combos = pd.MultiIndex.from_tuples(product(artists, venues), names=['artist', 'venue'])

# Reindex the columns to include all artist-venue pairs
grouped = grouped.reindex(columns=all_combos, fill_value=0)
grouped = grouped.sort_index(axis=1)
print(grouped)
