import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import datetime
from datetime import datetime
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler


%matplotlib inline
plt.style.use('fivethirtyeight')          #Used for replicating graph styles from fivethirtyeight.com

from keras.models import load_model

from binance.client import Client





#Loading the trained model
model = load_model('Bitcoin_model.h5')

#Summarize the model
model.summary()


#loading the data from Binance API
api_key = ""
secret_key = ""
client = Client(aki_key,secret_key)
check = client.get_klines(symbol='BTCUSDT',interval = Client.KLINE_INTERVAL_1MINUTE)



price = np.array([float(check[i][4]) for i in range(500)])
price = price.reshape(500,1)

scaler = StandardScaler()
scaler.fit(price[:374])

price = scaler.transform(price)



index = [496,497,498,499]

candles = scaler.transform(np.array([float(check[i][4]) for i in index]).reshape(-1,1))

model_feed = candles.reshape(1,4,1)

scaler.inverse_transform(model.predict(model_feed)[0])[0]
