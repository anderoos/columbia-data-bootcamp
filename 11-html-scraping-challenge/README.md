# CU-11-html-scraping-challenge
![mars-hero-image](https://www.mub.eps.manchester.ac.uk/science-engineering/wp-content/uploads/sites/59/2021/10/Mars-banner.jpg)
   
## Introduction
You’re now ready to take on a full web-scraping and data analysis project. You’ve learned to identify HTML elements on a page, identify their id and class attributes, and use this knowledge to extract information via both automated browsing with Splinter and HTML parsing with Beautiful Soup. You’ve also learned to scrape various types of information. These include HTML tables and recurring elements, like multiple news articles on a webpage.

As you work on this Challenge, remember that you’re strengthening the same core skills that you’ve been developing until now: collecting data, organizing and storing data, analyzing data, and then visually communicating your insights.

## Featured files
 * [Scraping Titles and Previews](https://github.com/anderoos/CU-11-html-scraping-challenge/blob/main/part_1_mars_news.ipynb)
 * [Scraping Mars Weather Data](https://github.com/anderoos/CU-11-html-scraping-challenge/blob/main/part_2_mars_weather.ipynb)
   
## Approaches and Resources
#### Data scaping:
 * Using BeautifulSoup, Splinter and Chromedriver, scaped recent news articles (in the provided website) of their titles and previews and stored them as a dictionary element. 
 * Additional tabular data recorded by Mar's Curiosity rover was scraped from the provided website and converted into tabular format by using BeautifullSoup, Splinter and Chromedriver.
   
#### Mars Weather Analayis 
 * Mars weather was analyized and tidied using pandas and visualized using matplotlib's pylot module and seaborn.
   
## Conclusions 
 * Months: 12
 * 1867 days (sols) of Martian data recorded.
 * Month three had the lowest average temperatures, and month eight had the highest average temperature.
 * Atmospheric pressure is, on average, lowest in the sixth month and highest in the ninth.
 * Martian year was estimated by finding the distance between peaks and troughs. Based on the data provided, on average, is a little over 681 sols, compared to the actual measure to 687 sols.

## Plots
![Average-temp-on-mars-by-month](https://github.com/anderoos/CU-11-html-scraping-challenge/blob/main/Images/temp_by_month.png)
![Average-pressure-on-mars-by-month](https://github.com/anderoos/CU-11-html-scraping-challenge/blob/main/Images/bar_by_month.png)
![Temperatures-recorded-by-sol](https://github.com/anderoos/CU-11-html-scraping-challenge/blob/main/Images/temp_by_sol.png)



