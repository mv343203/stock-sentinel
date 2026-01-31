import yfinance as yf
import torch
import pandas as pd
import numpy as np

# 1. Fetch 50 days of real history
ticker_symbol = "AAPL"
ticker = yf.Ticker(ticker_symbol)
# 'period' can be 1d, 5d, 1mo, 1y, etc. We'll use 3mo to ensure we get at least 50 trading days
df = ticker.history(period="3mo")

# 2. Extract only the 'Close' prices and take the last 50 days
# Stock markets are closed on weekends, so 3 months of data gives us plenty
close_prices = df['Close'].tail(50)

# 3. Clean the data (Crucial!)
# Convert to a 1D Numpy array first, then to a Float32 Tensor
price_array = close_prices.values.astype(np.float32)
history_tensor = torch.from_numpy(price_array)

print(f"📊 Successfully fetched 50 days of {ticker_symbol}")
print(f"📐 Tensor Shape: {history_tensor.shape}")
print(f"🔢 First 3 prices in Tensor: {history_tensor[:3]}")

# 4. Challenge: Simple Moving Average (SMA) in PyTorch
# Since it's a tensor, we can do math instantly!
sma_50 = history_tensor.mean()
print(f"📈 50-Day Moving Average: ${sma_50.item():.2f}")