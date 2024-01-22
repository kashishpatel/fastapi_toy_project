import httpx
import cachetools
from app.config.settings import settings

# Example of connecting to another API (https://github.com/fawazahmed0/currency-api)
CURRENCY_API_BASE_URL = settings.CURRENCY_API_BASE_URL

# Create an in-memory cache with a maximum size and TTL (time to live) for cached items
currency_cache = cachetools.TTLCache(maxsize=1000, ttl=3600)  # Cache for 1 hour

async def fetch_data_from_url(url):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            response.raise_for_status()  # Raise an exception for non-2xx status codes
            return response.json()
        except httpx.HTTPError as e:
            # Handle HTTP errors gracefully, e.g., log them and return None
            print(f"HTTP error occurred: {e}")
            return None

async def fetch_cached_data(key, url):
    # Try to get the data from the cache
    cached_data = currency_cache.get(key)
    
    if cached_data is not None:
        return cached_data

    data = await fetch_data_from_url(url)
    
    if data is not None:
        currency_cache[key] = data
    
    return data

async def fetch_available_currencies():
    url = CURRENCY_API_BASE_URL + 'currencies.json'
    return await fetch_cached_data("currencies", url)

async def fetch_all_exchange_rates(starting_currency):
    url = CURRENCY_API_BASE_URL + f'currencies/{starting_currency}.json'
    return await fetch_cached_data(f"{starting_currency}_all_rates", url)

async def fetch_exchange_rate(starting_currency, ending_currency):
    url = CURRENCY_API_BASE_URL + f'currencies/{starting_currency}/{ending_currency}.json'
    return await fetch_cached_data(f"{starting_currency}_{ending_currency}", url)
