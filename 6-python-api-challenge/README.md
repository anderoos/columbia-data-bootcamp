# CU-06-python-api-challenge
## Description
Using APIs and JSON traversals to answer the question: How does the weather change as we approach the equator?
#### WeatherPy
We are tasked to create a py script to visualize the weather of 500 cities of varying distances from the equator using citipy and OpenWeatherMap API to create a representative model of weathers across different cities. 
#### VacationPy

## Approaches and Resources
#### WeatherPy
* Use OpenWeatherMap to plot the northern and southern hemispheres with linear regression lines:
  * Latitude vs Temperature
  * Latitude vs Humidity
  * Latitude vs Cloudiness
  * Latitude vs Windspeed

#### VacationPy
* Use weather data to plan future vacations using the geoViews and Geoapify API and create a map visualization.
  * Create a map for every city with humidity
  * Narrow down the df to find the ideal weather condition
  * Create a new df to store city, country coordinates and humidity.
  * Use Geoapify API to find the first hotel within 10,000m
  * Add hotel name
## Conclusions
### WeatherPy
* **There is a strong relationship between maxiumum temperature and latitude**
![alt-text](https://github.com/anderoos/CU-6-python-api-challenge/blob/main/output_data/Fig1.png)
![alt-text](https://github.com/anderoos/CU-6-python-api-challenge/blob/main/output_data/Fig5.png)
![alt-text](https://github.com/anderoos/CU-6-python-api-challenge/blob/main/output_data/Fig6.png)

* **There is a weak relationship between relative humidity and latitude**
![alt-text](https://github.com/anderoos/CU-6-python-api-challenge/blob/main/output_data/Fig2.png)
![alt-text](https://github.com/anderoos/CU-6-python-api-challenge/blob/main/output_data/Fig7.png)
![alt-text](https://github.com/anderoos/CU-6-python-api-challenge/blob/main/output_data/Fig8.png)

* **There is a no relationship between cloudiness and latitude**
![alt-text](https://github.com/anderoos/CU-6-python-api-challenge/blob/main/output_data/Fig3.png)
![alt-text](https://github.com/anderoos/CU-6-python-api-challenge/blob/main/output_data/Fig9.png)
![alt-text](https://github.com/anderoos/CU-6-python-api-challenge/blob/main/output_data/Fig10.png)

* **There is a no relationship between wind speed and latitude**
![alt-text](https://github.com/anderoos/CU-6-python-api-challenge/blob/main/output_data/Fig4.png)
![alt-text](https://github.com/anderoos/CU-6-python-api-challenge/blob/main/output_data/Fig11.png)
![alt-text](https://github.com/anderoos/CU-6-python-api-challenge/blob/main/output_data/Fig12.png)

### VacationPy
![alt-text](https://github.com/anderoos/CU-6-python-api-challenge/blob/main/output_data/City_weather_with_humidity.png)
![alt-text](https://github.com/anderoos/CU-6-python-api-challenge/blob/main/output_data/Nearby_hotels_sorted_by_ideal_weather.png)
## Limitations and recommendations

## Licensing 
This code has no license restrictions. Challenge materials are provided by the Columbia School of Engineering.
