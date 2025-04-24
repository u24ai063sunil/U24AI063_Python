
import pandas as pd
asking_prices = pd.Series([10000, 12000, 13000, 8000, 15000])
fair_prices = pd.Series([11000, 11500, 13500, 9000, 15000])

good_deals = asking_prices < fair_prices
good_deal_indices = asking_prices[good_deals].index.tolist()

print("Good deal indices:", good_deal_indices)
