# py-example
Example FastAPI server that loads weather data from CSV using polars

## Local development

You must have poetry installed...

```
# Installing dependencies
$ poetry install

# Starting local server
$ poetry run uvicorn app:main:app --reload --lifespan on
```

## Running Python Tests
> Note: The tests are written against the weather_data.csv committed in the project

```
# Installing dependencies
$ poetry install

# Run pytest
$ poetry run pytest
```

## Weather Data
> Weather data from: https://github.com/vega/vega/blob/main/docs/data/seattle-weather.csv

Weather data should be stored with the following format under `weather_data.csv` in the root folder

Example:
```
date,precipitation,temp_max,temp_min,wind,weather
...
2012-06-03,0.0,17.2,9.4,2.9,sun
2012-06-04,1.3,12.8,8.9,3.1,rain
...
```

## API Schema

After running the local server, you can view the openapi schema at `http://127.0.0.1:8000/docs`


## Docker

Must have docker installed on local machine

### Build

`DOCKER_BUILDKIT=1 docker build --target=runtime . -t pyexample:latest`

### Running

`docker run -p 8000:8000 pyexample:latest`

### Testing with docker-compose & client

`docker-compose up`