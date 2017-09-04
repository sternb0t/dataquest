from datetime import datetime

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# read data, handle datetime col, and sort
df = pd.read_csv('sphist.csv')
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

# compute 3 indicators:
# 1 average price for past 5 days
# 2 average price for past 30 days
# 3 ratio between 1/2

df["close_avg_5"] = df["Close"].rolling(center=False, window=5).mean().shift(1)
df["close_avg_30"] = df["Close"].rolling(center=False, window=30).mean().shift(1)
df["close_ratio_avg_5_avg_30"] = df["close_avg_5"] / df["close_avg_30"]

# additional 2 indicators:

# 4 average volume over the past year
# 5 standard deviation of the average volume over the past year

df["vol_avg_365"] = df["Volume"].rolling(center=False, window=365).mean().shift(1)
df["vol_std_avg_365"] = df["vol_avg_365"].rolling(center=False, window=365).std().shift(1)


# remove old rows
before_1951 = df["Date"] < datetime(year=1951, month=1, day=3)
to_drop = df[before_1951].index
df = df.drop(to_drop, axis=0)
df = df.dropna(axis=0)

# split training and test

before_2013 = df["Date"] < datetime(year=2013, month=1, day=1)
after_2013 = df["Date"] >= datetime(year=2013, month=1, day=1)
train = df[before_2013]
test = df[after_2013]


# fit and test linear regression model

model = LinearRegression()

features = [
    "close_avg_5", 
    "close_avg_30", 
    "close_ratio_avg_5_avg_30",
    "vol_avg_365",
    "vol_std_avg_365"
]

target = "Close"

model.fit(train[features], train[target])

predictions = model.predict(test[features])

mae = mean_absolute_error(test[target], predictions)

print("mean absolute error:", mae)





