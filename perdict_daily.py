import pandas as pd
import numpy as np
import joblib
from datetime import datetime, timedelta

# Load trained model
model = joblib.load('tsla_model.pkl')

# Load your data
data = pd.read_csv('TSLA.csv')
data['Date'] = pd.to_datetime(data['Date'])
data.sort_values('Date', inplace=True)

# Calculate indicators
data['SMA_10'] = data['Close'].rolling(window=10).mean()
data['EMA_20'] = data['Close'].ewm(span=20, adjust=False).mean()
delta = data['Close'].diff()
gain = delta.where(delta > 0, 0).rolling(window=14).mean()
loss = -delta.where(delta < 0, 0).rolling(window=14).mean()
rs = gain / loss
data['RSI'] = 100 - (100 / (1 + rs))
data['MACD'] = data['Close'].ewm(span=12, adjust=False).mean() - data['Close'].ewm(span=26, adjust=False).mean()

data.dropna(inplace=True)

# Get latest available trading day's data
last_date = data['Date'].max()
latest_data = data[data['Date'] == last_date]

features = ['Open', 'High', 'Low', 'Close', 'Volume', 'SMA_10', 'EMA_20', 'RSI', 'MACD']
X_latest = latest_data[features]

# Make prediction
prediction = model.predict(X_latest)[0]

# Example trading logic
capital = 10000
fee = 0.01
price = latest_data['Close'].values[0]

# Example strategy: full capital usage
if prediction == 1:
    action = f"Buy: {capital * (1 - fee):.2f} USD worth of shares"
elif prediction == 0:
    action = f"Sell: ALL shares"
else:
    action = "Hold: No transaction"

print(f"Date: {last_date.date()} | Recommended action: {action}")
