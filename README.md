# Andrew Cheng - Columbia Data Analytics Bootcamp

## About
This repository serves to showcase my journey and skills in data analytics and visualization and a way to track progress and skills in analytics and data science related topics.

## Table of Contents
* [About](#about)
* [Challenge Assignments](#challenge-assignments)
  * [Analyzing Crowdfunding Data with Excel](#analyzing-crowdfunding-data-with-excel)
  * [Analyzing Stocks with VBA](#analyzing-stocks-with-vba)
  * [Poll and Finance analysis with Python](#poll-and-finance-analysis-with-python)
  * [Aggregate analysis of Student Performance with Pandas](#aggregate-analysis-of-student-performance-with-pandas)
  * [Visualizing drug efficacy with Matplotlib](#visualizing-drug-efficacy-with-matplotlib)
  * [Visualizing weather data with WeatherPy](#visualizing-weather-data-with-weatherpy)
  * [Data Engineering with SQL](#data-engineering-with-sql)
  * [Querying with SQLalchemy](#querying-with-sqlalchemy)
  * [Web scraping Mars Weather Data](#web-scraping-mars-weather-data)
  * [Querying with Mongo and Pymongo](#querying-with-mongo-and-pymongo)
  * [Dashboarding Bellybutton Microbiome Plotly](#dashboarding-bellybutton-microbiome-plotly)
  * [Dashboarding Earthquake Data with Leaflet](#dashboarding-earthquake-data-with-leaflet)
  * [Visualizing Citibike Data with Tableau](#visualizing-citibike-data-with-tableau)
  * [Unsupervised ML with Cryptocurreny Data](#unsupervised-ml-with-cryptocurreny-data)
  * [Credit Risk Classification Report with Logistic Regression](#credit-risk-classification-report-with-logistic-regression)
  * [Investment Opportunities with Tensorflow](#investment-opportunities-with-tensorflow)
  * [Investigating Home Sales prices with PySpark and Parquet](#investigating-home-sales-prices-with-pyspark-and-parquet)
* [Milestone Projects](#milestone-projects)
  * [Property Investment Opportunities in 2025](https://github.com/anderoos/property-investment-ops-2025)
  * [Crowdfunding ETL Project](https://github.com/anderoos/crowdfunding-ETL)
  * [Visualizing Electricty Usage and Rates](https://github.com/ElenaLomako/Project-3/tree/main)
  * [Segmenting Customers with E-Commerce Data](https://github.com/anderoos/customer-segmentation)
* [Contact](#contact)

## Challenge Assignments
### Analyzing Crowdfunding Data with Excel
**Code/ Folder:** [01-excel-challenge](https://github.com/anderoos/columbia-data-bootcamp/tree/main/01-excel-challenge)  <br>
**Description:** The goal of this challenge is become acquainted with manipulating tabular data in Excel.<br>
**Tech-stack:** `excel`<br>
**Results:** [Report](https://github.com/anderoos/columbia-data-bootcamp/blob/main/01-excel-challenge/1.0%20Crowdfunding%20summary.docx) <br> 
<br>

### Analyzing Stocks with VBA
**Code/ Folder:** [02-vba-challenge](https://github.com/anderoos/columbia-data-bootcamp/tree/main/02-vba-challenge)<br>
**Description:** Analyzing historic stock data using VBA scripting to identify largest movers.<br>
**Tech-stack:** `excel`, `vba`<br>
<br>

### Poll and Finance analysis with Python
**Code/ Folder:** [03-python-challenge](https://github.com/anderoos/columbia-data-bootcamp/tree/main/03-python-challenge)<br>
**Description:** Using basic python scripting, analyze datasets to output financial and polling data.<br>
**Tech-stack:**  `python`<br>
<br>

### Aggregate analysis of Student Performance with Pandas
**Code/ Folder:** [04-pandas-challenge](https://github.com/anderoos/columbia-data-bootcamp/tree/main/04-pandas-challenge)<br>
**Description:** In this dataset, we are exploring tabular data with the pandas library to investigate how charter schools perform against district schools with budget considerations. <br>
**Tech-stack:**  `python`, `pandas`
**Results:** Charter schools generally perform better than district schools in this city. Budget appears to have an inverse effect on performance; lower performing schools have a budget of about $650 per student, compared to higher performing schools with a budget below $635 per student. Student population has a strong effect on performance: top 5 performing schools had a student population less than 2500, and bottom performing schools having more than 2900 students. <br>
<br>

### Visualizing drug efficacy with Matplotlib
**Code/ Folder:** [05-data-visualization-challenge](https://github.com/anderoos/columbia-data-bootcamp/tree/main/05-data-visualization-challenge)<br>
**Description:**: In this fictional dataset, we are screening for potential treatment candidates for squamous cell carcinoma (SCC). We are given a dataset containing the most recent animal study in mice. In this dataset, researchers have identified 249 mice with SCC tumors and received treatment regimens. Over the course of 45 days, weight, tumor volume and metastatic sites were recorded in 5 day intervals. The purpose of this study is to compare the drug of interest Capomulin, against other treatment regimens.<br>
**Tech-stack:**  `python`, `pandas`, `matplotlib`, `seaborn`<br>
**Results:** Capomulin & Ramicane have the most observations. Study design has a near equal amount of male and female subjects. Capomulin & Ramicane is the most effective in reducing tumor volume in mouse models over a 45 day period. Capomulin is effective in reducing tumor volume when compared to mouse weight over a 45 day period. In the Capomulin cohort, there is a strong correlation between Mouse weight and final tumor volume, suggesting that tumor size correlates with the weight of the mouse, pvalues shows that it is statistically significant.<br>
<br>

### Visualizing weather data with WeatherPy
**Code/ Folder:** [06-python-api-challenge](https://github.com/anderoos/columbia-data-bootcamp/tree/main/06-python-api-challenge)<br>
**Description:** We are tasked to create a py script to visualize the weather of 500 cities of varying distances from the equator using citipy and OpenWeatherMap API to create a representative model of weathers across different cities.<br>
**Tech-stack:** `python`, `pandas`, `numpy`, `scipy`, `requests`<br>
**Results:** There is a strong relationship between maxiumum temperature and latitude. There is a weak relationship between relative humidity and latitude. There is a no relationship between cloudiness and latitude.<br>
<br>

### Data Engineering with SQL
**Code/ Folder:** [09-sql-challenge](https://github.com/anderoos/columbia-data-bootcamp/tree/main/09-sql-challenge)<br>
**Description:** It’s been two weeks since you were hired as a new data engineer at Pewlett Hackard (a fictional company). Your first major task is to do a research project about people whom the company employed during the 1980s and 1990s. All that remains of the employee database from that period are six CSV files. For this project, you’ll design the tables to hold the data from the CSV files, import the CSV files into a SQL database, and then answer questions about the data. That is, you’ll perform data modeling, data engineering, and data analysis, respectively. Using APIs and JSON traversals to answer the question: How does the weather change as we approach the equator?<br>
**Tech-stack:**  `postgresql`, `pgadmin4`, `sql`<br>
<br>

### Querying with SQLalchemy
**Code/ Folder:** [10-sqlalchemy-challenge](https://github.com/anderoos/columbia-data-bootcamp/tree/main/10-sqlalchemy-challenge)
**Description:** Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii. To help with your trip planning, you decide to do a climate analysis about the area. The following sections outline the steps that you need to take to accomplish this task.<br>
**Tech-stack:**  `python`, `sql`, `sqlalchemy`, `matplotlib`<br>
**Results:** The average temperature between 2016 and 2017 is 73.1F, with median temperatuer at 74.0F<br>
<br>

### Web scraping Mars Weather Data
**Code/ Folder:** [11-html-scraping-challenge](https://github.com/anderoos/columbia-data-bootcamp/tree/main/11-html-scraping-challenge)
**Description:** You’re now ready to take on a full web-scraping and data analysis project. You’ve learned to identify HTML elements on a page, identify their id and class attributes, and use this knowledge to extract information via both automated browsing with Splinter and HTML parsing with Beautiful Soup. You’ve also learned to scrape various types of information. These include HTML tables and recurring elements, like multiple news articles on a webpage.<br>
**Tech-stack:**  `python`, `bs4`, `matplotlib`, `seaborn`<br>
**Results:** Atmospheric pressure experienced is lowest the sixth month and highest in the ninth. One martian year is observed to be 681 martian sols.<br>
<br>

### Querying with Mongo and Pymongo
**Code/ Folder:** [12-noSQL-challenge](https://github.com/anderoos/columbia-data-bootcamp/tree/main/12-noSQL-challenge)<br>
**Description:**  The UK Food Standards Agency evaluates various establishments across the United Kingdom, and gives them a food hygiene rating. You've been contracted by the editors of a food magazine, Eat Safe, Love, to evaluate some of the ratings data in order to help their journalists and food critics decide where to focus future articles.<br>
**Tech-stack:**  `MongoDB`, `Mongo Atlas`, `pymongo`<br>
**Results:** Most unhygenic restaurants: 41 count. Highest rated restaurants in London Area: 33 count. Highest rated restaurants in a 0.01 Long/Lat radius of Penang Flavours: 87<br>
<br>

### Dashboarding Bellybutton Microbiome Plotly
**Code/ Folder:** [14-belly-button-challenge](https://github.com/anderoos/columbia-data-bootcamp/tree/main/14-belly-button-challenge)<br>
**Description:** Building interactive dashboards of bellybutton microbome using D3 and Javascript<br>
**Tech-stack:**  `javascript`, `d3`<br>
<br>

### Dashboarding Earthquake Data with Leaflet
**Code/ Folder:** [15-leaflet-challenge](https://github.com/anderoos/columbia-data-bootcamp/tree/main/15-leaflet-challenge)<br>
**Description:**The United States Geological Survey, or USGS for short, is responsible for providing scientific data about natural hazards, the health of our ecosystems and environment, and the impacts of climate and land-use change. Their scientists develop new methods and tools to supply timely, relevant, and useful information about the Earth and its processes. The USGS is interested in building a new set of tools that will allow them to visualize their earthquake data. They collect a massive amount of data from all over the world each day, but they lack a meaningful way of displaying it. In this challenge, you have been tasked with developing a way to visualize USGS data that will allow them to better educate the public and other government organizations (and hopefully secure more funding) on issues facing our planet.<br>
**Tech-stack:**  `javascript`, `d3`, `leaflet`<br>
<br>

### Visualizing Citibike Data with Tableau
**Code/ Folder:** [16-tableau-challenge](https://github.com/anderoos/columbia-data-bootcamp/tree/main/16-tableau-challenge)<br>
**Description:** Visualizing and dashboarding two months of citibike data.<br>
**Tech-stack:**  `tableau`<br>
**Results:** [Tableau Public Link](https://public.tableau.com/app/profile/andrew.cheng1065/viz/citibike-nov/Dashboard1)<br>
<br>

### Unsupervised ML with Cryptocurreny Data
**Code/ Folder:** [19-cryptoclustering](https://github.com/anderoos/columbia-data-bootcamp/tree/main/19-cryptoclustering)<br>
**Tech-stack:**  Cryptocurrencies has been gaining popularity since the early 2010's. In this challenge project, using a unsupervised machine learning learning method PCA and KMeans clustering, predict the relationship between the price change at 24 hours versus 7 days.<br>
**Tech-stack:**  `python`, `sklearn`, `hvplot`<br>
<br>

### Credit Risk Classification Report with Logistic Regression
**Code/ Folder:** [20-credit-risk-classification](https://github.com/anderoos/columbia-data-bootcamp/tree/main/20-credit-risk-classification)<br>
**Description:** The goal of this analysis is to build a classification model using logistic regression algorithm to predict high risk lenders and healthy low risk lenders. This model was trained using historical peer to peer lending activity. This data contains loan information like loan size, interest rate, borrower income, debt, account and derogatory marks on credit.<br>
**Tech-stack:** `sklearn`, `seaborn`, `python`<br>
**Results:** Both models display high classification power based on the ROC-AUC curve. Random oversampling algorithm was successful in improving classification prediction and yielded more favorable results when compared to classify imbalanced labels. In our second model when we employed random oversampling algorithm from imblearn (here called ros) we achieved balanced_accuracy_score and accuracy score of 99%. Although this model experienced a modest reduction in precision, this model overall improved recall and F1 by 9% and 3% respectively. Its worth noting lowered precision is probably acceptable within this context. As a bank attempting to assess the creditworthiness of borrowers, misidentifying high-risk borrowers is is more judicious than identifying low-risk borrowers to help mitigate lending risk.<br>
<br>

### Investment Opportunities with Tensorflow
**Code/ Folder:** [21-deep-learning-challenge](https://github.com/anderoos/columbia-data-bootcamp/tree/main/21-deep-learning-challenge)<br>
**Description:** The nonprofit foundation Alphabet Soup wants a tool that can help it select the applicants for funding with the best chance of success in their ventures. With your knowledge of machine learning and neural networks, you’ll use the features in the provided dataset to create a binary classifier that can predict whether applicants will be successful if funded by Alphabet Soup.<br>
**Tech-stack:** `tensorflow`, `python`<br>
**Results:** Model 1.2b achieved an accuracy score of 82.9% with a loss ratio of 0.40. Using a combination of sigmoid and relu activation functions, baseline accuracy was established at 74%. Despite this large dataset, additional features such as NAME improved model accuracy, suggesting branding/marketing may play a role in the success of the business.<br>
<br>

### Investigating Home Sales prices with PySpark and Parquet
**Code/ Folder:** [22-pyspark-challenge](https://github.com/anderoos/columbia-data-bootcamp/tree/main/22-pyspark-challenge)<br>
**Description:** Querying data with pyspark and Databricks.<br>
**Tech-stack:**  `pyspark`, `hdfs`, `python`, `databricks`<br>
<br>

## Milestone Projects
  * [Property Investment Opportunities in 2025](https://github.com/anderoos/property-investment-ops-2025)
  * [Crowdfunding ETL Project](https://github.com/anderoos/crowdfunding-ETL)
  * [Visualizing Electricty Usage and Rates](https://github.com/ElenaLomako/Project-3/tree/main)
  * [Segmenting Customers with E-Commerce Data](https://github.com/anderoos/customer-segmentation)
<br>
    
## Contact
[Github](https://github.com/anderoos)<br>
[Linkedin](https://www.linkedin.com/in/andrew-cheng14/)
