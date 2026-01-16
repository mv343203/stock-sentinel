from pydantic import BaseModel, Field, field_validator
from datetime import datetime
from typing import Optional

# 1. Define the 'bouncer' (The Model)
class StockQuote(BaseModel): # Model for stock quote data inheriting from Pydantic
    symbol: str = Field(..., min_length=1, max_length=5) #Field() is limited to simple, built-in validation rules. Anything more complex (like calling a method) requires the decorato
    price: float = Field(..., gt=0) # Price must be Greater Than 0
    volume: int = Field(..., ge=0)  # Volume must be Greater or Equal to 0
    timestamp: datetime = Field(default_factory=datetime.now)
    exchange: Optional[str] = "NASDAQ"

    # 2. Add a custom rule
    @field_validator('symbol') #validator for the 'symbol' field meaning it will validate the 'symbol' field
    @classmethod #decorator to indicate this is a class method meaning it receives the class as the first argument
    def ticker_must_be_uppercase(cls, v: str) -> str:
        if not v.isupper():
            raise ValueError('Ticker symbol must be all uppercase (e.g., AAPL)')
        return v

# 3. Test it out with "Raw Data"
raw_data = {
    "symbol": "AAPL",
    "price": 175.50,
    "volume": 50000000
}

try:
    # This creates a validated object
    quote = StockQuote(**raw_data)
    print(f"✅ Validation Successful: {quote.symbol} is trading at ${quote.price}")
    print(f"Full Object: {quote.model_dump_json(indent=2)}")
except Exception as e:
    print(f"❌ Validation Failed: {e}")