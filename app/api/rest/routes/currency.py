from fastapi import APIRouter, Depends, HTTPException
from app.utils.jwt_auth import verify_jwt_token
from ...schemas.currency import (
    CurrencyResponse,
    ExchangeRatePair,
    ExchangeRateResponse,
    AllExchangeRatesResponse,
)
from app.integrations.currency_api import (
    fetch_available_currencies,
    fetch_exchange_rate,
    fetch_all_exchange_rates,
)

router = APIRouter(tags=["Integrating External Currency API"])

async def fetch_currency_data():
    currency_data = await fetch_available_currencies()
    if currency_data is None:
        raise HTTPException(status_code=500, detail="Failed to fetch available currencies")
    return currency_data

@router.get("/available_currencies", response_model=list[CurrencyResponse])
async def get_available_currencies(current_user: str = Depends(verify_jwt_token)):
    currency_data = await fetch_currency_data()
    available_currencies = [CurrencyResponse(abbreviation=k, name=v) for k, v in currency_data.items()]
    return available_currencies

@router.get("/all_exchange_rates/{starting_currency}", response_model=AllExchangeRatesResponse)
async def get_all_exchange_rates(starting_currency: str, current_user: str = Depends(verify_jwt_token)):
    currency_data = await fetch_currency_data()
    available_currencies = list(currency_data.keys())
    starting_currency = starting_currency.lower()
    
    if starting_currency not in available_currencies:
        raise HTTPException(status_code=400, detail="Invalid starting currency")
    
    exchange_rates = await fetch_all_exchange_rates(starting_currency)
    
    if not exchange_rates:
        raise HTTPException(status_code=404, detail="No exchange rates found")
    
    date = exchange_rates["date"]
    rates = exchange_rates[starting_currency]
    
    return AllExchangeRatesResponse(
        date=date,
        starting_currency=currency_data.get(starting_currency, starting_currency),
        exchange_rates=rates,
    )

@router.post("/exchange_rate", response_model=ExchangeRateResponse)
async def get_exchange_rate(pair: ExchangeRatePair, current_user: str = Depends(verify_jwt_token)):
    currency_data = await fetch_currency_data()
    available_currencies = list(currency_data.keys())
    starting_currency = pair.starting_currency.lower()
    ending_currency = pair.ending_currency.lower()
    
    if starting_currency not in available_currencies or ending_currency not in available_currencies:
        raise HTTPException(status_code=400, detail="Invalid currency pair")
    
    response_json = await fetch_exchange_rate(starting_currency, ending_currency)
    
    if response_json is None:
        raise HTTPException(status_code=404, detail="Currency pair not found")
    
    return ExchangeRateResponse(
        date=response_json["date"],
        starting_currency=currency_data.get(starting_currency, starting_currency),
        ending_currency=currency_data.get(ending_currency, ending_currency),
        rate=response_json[ending_currency],
    )
