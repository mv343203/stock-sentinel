import asyncio
import random
from datetime import datetime
from schemas import StockQuote  # Importing the 'bouncer' you made earlier

# 1. Simulate an Async API call
async def fetch_stock_data(ticker: str) -> StockQuote:
    print(f"📡 Requesting data for {ticker}...")
    
    # Simulate network delay (1 to 3 seconds)
    # We use 'await asyncio.sleep' instead of 'time.sleep' so the program doesn't freeze
    await asyncio.sleep(random.uniform(1, 3)) 
    
    # Simulated raw data from an API
    raw_data = {
        "symbol": ticker.upper(),
        "price": round(random.uniform(150, 200), 2),
        "volume": random.randint(1000000, 5000000)
    }
    
    # Validate with Pydantic
    return StockQuote(**raw_data)

# 2. The main 'Traffic Controller'
async def main():
    start_time = datetime.now()
    tickers = ["AAPL", "TSLA", "MSFT", "NVDA", "GOOGL"]
    
    print(f"🚀 Starting concurrent fetch for: {tickers}")
    
    # 'Gather' runs all these requests at the same time
    results = await asyncio.gather(*(fetch_stock_data(t) for t in tickers))
    
    print("-" * 30)
    for quote in results:
        print(f"📈 {quote.symbol}: ${quote.price} (Vol: {quote.volume})")
    
    end_time = datetime.now()
    print(f"\n⏱️ Total time taken: {(end_time - start_time).total_seconds():.2f} seconds")
    print(" (Notice this is much faster than fetching them one-by-one!)")

if __name__ == "__main__":
    asyncio.run(main())