from pydantic import BaseModel
from typing import Dict

class CurrencyResponse(BaseModel):
    name: str
    abbreviation: str

class ExchangeRatePair(BaseModel):
    starting_currency: str
    ending_currency: str

class ExchangeRateResponse(BaseModel):
    date: str
    starting_currency: str
    ending_currency: str
    rate: float

class AllExchangeRatesResponse(BaseModel):
    date: str
    starting_currency: str
    exchange_rates: Dict[str, float]