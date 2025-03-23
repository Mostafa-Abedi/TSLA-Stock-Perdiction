import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
import joblib

# Load and preprocess data
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

# Target (next-day movement)
data['Target'] = (data['Close'].shift(-1) > data['Close']).astype(int)

# Drop NaNs
data.dropna(inplace=True)

# Features and target
features = ['Open', 'High', 'Low', 'Close', 'Volume', 'SMA_10', 'EMA_20', 'RSI', 'MACD']
X = data[features]
y = data['Target']

# Split and train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'tsla_model.pkl')

print("Model training complete and saved as 'tsla_model.pkl'")