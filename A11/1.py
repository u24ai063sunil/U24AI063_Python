import pandas as pd
import datetime

# a) Date time object for Jan 15, 2012
dt1 = pd.Timestamp('2012-01-15')
# b) Specific date and time of 9:20 pm
dt2 = pd.Timestamp('2023-01-01 21:20:00')  # use any specific date

# c) Local date and time
dt3 = pd.Timestamp.now()

# d) A date without time
dt4 = pd.to_datetime('2023-05-01').date()

# e) Current date
dt5 = pd.Timestamp.today().date()

# f) Time from a datetime
dt6 = pd.Timestamp.now().time()

# g) Current local time
dt7 = datetime.datetime.now().time()

print(dt1,"\n", dt2,"\n", dt3,"\n", dt4,"\n", dt5,"\n", dt6,"\n", dt7)
