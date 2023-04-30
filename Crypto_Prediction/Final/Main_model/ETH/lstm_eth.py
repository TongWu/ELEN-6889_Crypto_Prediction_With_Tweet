# -*- coding: utf-8 -*-
"""LSTM-ETH.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vg71OJCbZPSXgzv04rF5Yh2BDVbbXczw
"""

import math
import yfinance as yf
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import datetime

# Fetch ETH trade raw data
today = datetime.date.today()
ETH_raw = yf.download('ETH-USD', start=today-datetime.timedelta(days=700), end=today)
# Split the raw data into parts
ETH_basic = ETH_raw[['Adj Close', 'Open']]
ETH_quant = ETH_raw

plt.figure(figsize=(15, 8))
plt.title('ETH Prices History')
plt.plot(ETH_quant['Adj Close'])
plt.xlabel('Date')
plt.ylabel('Prices ($)')

### The code below is for merge sentimental data ONLY
### The code contains the merge, split train and test data, and train the model
### The code will be commented until the sentimental data is fetched
def merge_sentimental_data(sentimental_data_file_path, ETH_data):
  # Load sentimental data in csv
  sentiment_data = pd.read_csv(sentimental_data_file_path).iloc[:, 1]
  # sentiment_data = pd.DataFrame(0, index=range(23), columns=sentiment_data.columns)
  zeros = pd.DataFrame([0]*21)
  sentiment_data = pd.concat([zeros, sentiment_data], ignore_index=True)

  # Merge with ETH quant
  merged_data = pd.concat([ETH_data, sentiment_data], axis=1)
  num_rows = len(ETH_data)

  # 创建一个与other_data索引长度相同的全0 DataFrame
  new_data_adjusted = pd.DataFrame([0] * num_rows, index=ETH_data.index)

  # 从底部开始填充sentiment_data的值
  new_data_adjusted.iloc[-len(sentiment_data):] = sentiment_data.values

  # 将new_data_adjusted添加到ETH_quant作为新的一列
  merged_data = pd.concat([ETH_data, new_data_adjusted], axis=1)
  merged_data.columns = list(ETH_data.columns) + ['sentiment']
  return merged_data

### The code below is for merge sentimental data ONLY
### The code contains the merge, split train and test data, and train the model
### The code will be commented until the sentimental data is fetched

sentimental_data_file_path = './ETH_vader.csv'
ETH_data = ETH_quant
merged_data = merge_sentimental_data(sentimental_data_file_path, ETH_data)

# Normalise data, if necessary
price_data = merged_data['Adj Close'].values.reshape(-1, 1)
sentiment_data = merged_data['sentiment'].values.reshape(-1, 1)

scaler = MinMaxScaler(feature_range=(0, 1))
scaler_sentiment = MinMaxScaler(feature_range=(0, 1))

scaled_price_data = scaler.fit_transform(price_data)
scaled_sentiment_data = scaler_sentiment.fit_transform(sentiment_data)
# Create window size
def create_dataset(price_dataset, sentiment_dataset, look_back=1, sentiment_weight=0.01):
    x_train, y_train = [], []
    for i in range(len(price_dataset) - look_back - 1):
        x_train.append(np.hstack((price_dataset[i:(i + look_back), 0], sentiment_weight * sentiment_dataset[i:(i + look_back), 0])))
        y_train.append(price_dataset[i + look_back, 0])
    return np.array(x_train), np.array(y_train)


training_data_len = math.ceil(len(scaled_price_data) * 0.8)
training_price_data = scaled_price_data[0: training_data_len, :]
training_sentiment_data = scaled_sentiment_data[0: training_data_len, :]

# Create train set
window_size = 30
x_train, y_train = create_dataset(training_price_data, training_sentiment_data, window_size)
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

# Create test set
test_price_data = scaled_price_data[training_data_len - window_size:, :]
test_sentiment_data = scaled_sentiment_data[training_data_len - window_size:, :]

x_test, y_test = create_dataset(test_price_data, test_sentiment_data, window_size)
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
y_test = ETH_quant['Adj Close'].values[training_data_len:]

model = keras.Sequential()
model.add(layers.LSTM(units=30, return_sequences=True, input_shape=(x_train.shape[1], 1)))
model.add(layers.Dropout(0.3))

model.add(layers.GRU(units=30, return_sequences=True))  # GRU layer
model.add(layers.Dropout(0.3))

model.add(layers.LSTM(units=30, return_sequences=True))
model.add(layers.Dropout(0.3))

model.add(layers.LSTM(units=30))
model.add(layers.Dropout(0.3))

model.add(layers.Dense(units=1))
model.summary()

from google.colab import drive
drive.mount('/content/drive')

# Grid Search
"""
from tensorflow.keras import layers, optimizers
from tensorflow.keras.wrappers.scikit_learn import KerasRegressor

def create_model(optimizer=keras.optimizers.Adam(learning_rate=0.005, amsgrad=True), dropout_rate=0.3, units=30):
    model = keras.Sequential()
    model.add(layers.LSTM(units=units, return_sequences=True, input_shape=(x_train.shape[1], 1)))
    model.add(layers.Dropout(dropout_rate))
    
    model.add(layers.GRU(units=units, return_sequences=True))  # GRU layer
    model.add(layers.Dropout(dropout_rate))
    
    model.add(layers.LSTM(units=units, return_sequences=True))
    model.add(layers.Dropout(dropout_rate))
    
    model.add(layers.LSTM(units=units))
    model.add(layers.Dropout(dropout_rate))
    
    model.add(layers.Dense(units=1))
    model.compile(optimizer=optimizer, loss='mse', metrics=['accuracy'])
    return model
model = KerasRegressor(build_fn=create_model, verbose=0)
param_grid = {
    'optimizer': ['adam', 'rmsprop', 'amsgrad'],
    'dropout_rate': [0.0, 0.1, 0.2, 0.3],
    'units': [30, 50, 70],
    'batch_size': [8, 16, 32, 64],
    'epochs': [50, 100]
}
from sklearn.model_selection import GridSearchCV

grid = GridSearchCV(estimator=model, param_grid=param_grid, n_jobs=1, cv=3)
grid_result = grid.fit(x_train, y_train)
print("Best score: %f using %s" % (grid_result.best_score_, grid_result.best_params_))
"""

### Traning ###
model.compile(optimizer=keras.optimizers.Adam(learning_rate=0.005, amsgrad=True), loss='mean_squared_error')
model.fit(x_train, y_train, batch_size= 32, epochs=100)
model.save(f'./ETH_model.h5')

predictions = model.predict(x_test)
predictions = scaler.inverse_transform(predictions)
rmse = np.sqrt(np.mean(predictions - y_test)**2)
rmse

data = ETH_quant.filter(['Adj Close'])
train = data[:training_data_len]
validation = data[training_data_len+1:]
validation['Predictions'] = predictions
plt.figure(figsize=(16,8))
plt.title('Model')
plt.xlabel('Date')
plt.ylabel('Close Price USD ($)')
plt.plot(train)
plt.plot(validation[['Adj Close', 'Predictions']])
plt.legend(['Train', 'Original', 'Predictions'], loc='lower right')
plt.savefig('./ETH_Result.png', dpi=300, bbox_inches='tight')
plt.show()

file_path='./ETH_prediction.csv'
validation.to_csv(file_path, index=False)

### The code below is for dataset that merge sentimental data ONLY
### The code will be commented until the sentimental data is fetched
error = validation.iloc[-1, 0] - validation.iloc[-1, 1]
def predict(num_days_to_predict, sentimental_data_file_path):
    ### Fetch ETH-USD data BEGIN ###
    ### CHANGE THIS TO THE FUNCTION USING PYSPARK ###
    today = datetime.date.today()
    ETH_quant = yf.download('ETH-USD', start=today-datetime.timedelta(days=365), end=today)
    ### Fetch ETH-USD data END ###
    new_df=ETH_quant.filter(['Adj Close'])
    # Merge sentimental data
    merged_data = merge_sentimental_data(sentimental_data_file_path, new_df)
    # Create 30 window days slot
    last_30_days = merged_data[-30:].values
    last_30_days_price = merged_data['Adj Close'][-30:].values.reshape(-1, 1)
    last_30_days_sentiment = merged_data['sentiment'][-30:].values.reshape(-1, 1)
    scaler = MinMaxScaler()
    last_30_days_scaled_price = scaler.fit_transform(last_30_days_price)
    sentiment_data = pd.read_csv(sentimental_data_file_path).iloc[:, 1]
    sentiment_values = sentiment_data.values.reshape(-1, 1)
    scaler_sentiment = MinMaxScaler()
    scaled_sentiment = scaler_sentiment.fit_transform(sentiment_values)
    last_30_days_scaled_sentiment = scaler_sentiment.transform(last_30_days_sentiment)
    predictions = []
    predicted_dates = []
    # Predict price
    for _ in range(num_days_to_predict):
        offset = error*(0.5-0.03*_)
        if (offset<0):
          offset = 0
        last_date = merged_data.index[-1]
        X_test = []
        X_test.append(np.hstack((last_30_days_scaled_price.flatten(), last_30_days_scaled_sentiment.flatten())))
        X_test = np.array(X_test)
        X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
        pred_price = model.predict(X_test)
        pred_price_unscaled = scaler.inverse_transform(pred_price)
        predictions.append(pred_price_unscaled[0][0]+offset)
        last_30_days_scaled_price = np.concatenate((last_30_days_scaled_price[1:], pred_price), axis=0)
        predicted_date = last_date + datetime.timedelta(days=_+1)
        predicted_dates.append(predicted_date)
    # print(f"Price of ETH-USD for the next {num_days_to_predict} trading days: {predictions}")
    output_text = f"Price of ETH-USD for the next {num_days_to_predict} trading days: {predictions}"
    print(output_text)
    # file_name = f"./public/ETH/Prediction_{num_days_to_predict}days.txt"
    # with open(file_name, 'w') as file:
      # file.write(output_text)
    fig, ax = plt.subplots()
    ax.plot(predicted_dates, predictions, marker='o', label='Predicted Prices')
    ax.set(xlabel='Date', ylabel='ETH-USD Price', title=f'Predicted ETH-USD Prices for the Next {num_days_to_predict} Trading Days')
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
    ax.set_xlim(predicted_dates[0] - datetime.timedelta(days=2), predicted_dates[0] + datetime.timedelta(days=num_days_to_predict+3))
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid()
    # plt.savefig(f'/src/Components/ETH/Prediction_{num_days_to_predict}days', dpi=300, bbox_inches='tight')
    plt.show()

sentimental_data_file_path = './ETH_vader.csv'
predict(1, sentimental_data_file_path)

predict(3, sentimental_data_file_path)

predict(5, sentimental_data_file_path)

predict(30, sentimental_data_file_path)