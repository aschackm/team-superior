
import tabpy_client
client = tabpy_client.Client('http://localhost:9004/')
import pandas as pd
import numpy as np
import os
from sklearn.linear_model import LinearRegression

def price_score(X,y):
    model = LinearRegression()
    return model.fit(X, y)

def get_data():
    df = pd.read_csv(os.path.join("wineData.csv"))
    df.head()
    price_df = df[["points", "price"]]
    price_df = price_df[~price_df.isin(['NaN']).any(axis=1)]
    price_df.count()
    X = price_df.points.values.reshape(-1, 1)
    y = price_df.price.values.reshape(-1, 1)
    price_score(X,y)

client.deploy(get_data, get_data)