import pandas as pd
data = {
    'John': [False, True, False, True, False, False, True, False, False, True],
    'Judy': [False, True, True, False, False, True, False, False, False, True]
}
df = pd.DataFrame(data)

party_days = df['John'] & df['Judy']
days_til_party = []

for i in range(len(party_days)):
    future = party_days[i:]
    next_party = (future.index[future].tolist() or [len(party_days)])[0]
    days_til_party.append(next_party - i)

df['days_til_party'] = days_til_party
print(df)
