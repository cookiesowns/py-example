from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
import polars as pl

data = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the CSV
    try:
        data['weather_data'] = pl.read_csv("weather_data.csv")
    except FileNotFoundError:
        data['error'] = True
        print("Missing weather_data.csv, please make sure it exists")
    data['error'] = False
    yield
    # cleanup weather_data
    data.clear()

app = FastAPI(lifespan=lifespan)
@app.get("/")
async def root():
    if data['error']:
        raise HTTPException(status_code=500, detail="No weather data loaded")

    return {'results': list(data['weather_data'].iter_rows(named=True))}

@app.get('/query')
async def query(limit: int = 0, date: str = "", weather: str = ""):
    if data['error']:
        raise HTTPException(status_code=500, detail="No weather data loaded")
    
    filters = query_filters(date, weather)

    if limit > 0 and filters:
        return {'results': list(data['weather_data'].filter(filters['predicate']).limit(limit).iter_rows(named=True))}
    elif filters:
        return {'results': list(data['weather_data'].filter(filters['predicate']).iter_rows(named=True))}
    elif limit > 0 and not filters:
        return {'results': list(data['weather_data'].limit(limit).iter_rows(named=True))}
    else:
        return {'results': list(data['weather_data'].iter_rows(named=True))}
    
def query_filters(date: str, weather: str):
    if date and weather:
        return {'predicate': (pl.col('date') == date) & (pl.col('weather') == weather)}
    elif weather and not date:
        return {'predicate': (pl.col('weather') == weather)}
    elif date and not weather:
        return {'predicate': (pl.col('date') == date)}
    else:
        False
