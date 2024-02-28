# CU-11-html-scraping-challenge
![mongo-hero-image](https://webimages.mongodb.com/_com_assets/cms/kuzt9r42or1fxvlq2-Meta_Generic.png)
   
## Introduction
The UK Food Standards Agency evaluates various establishments across the United Kingdom, and gives them a food hygiene rating. You've been contracted by the editors of a food magazine, Eat Safe, Love, to evaluate some of the ratings data in order to help their journalists and food critics decide where to focus future articles.

## Dependencies 
```pymongo 4.6.0```
    
## Featured files
 * [Mongo Setup](https://github.com/anderoos/CU-12-noSQL-challenge/blob/main/NoSQL_setup_starter.ipynb)
 * [Analysis](https://github.com/anderoos/CU-12-noSQL-challenge/blob/main/NoSQL_analysis_starter.ipynb)
   
## Approaches and Resources
#### Data Setup:
 * Using pymongo to interface with a local database to create, read, update, delete documents in a collection named 'establishments'. 
 * Using a mix of queries, inserted new documents into the collection, modified and filtered data, as well as removed irrelevant information.
   
#### Analysis starter
 * Exploratory analysis was performed based on the grading rubric. Identified businesses in the London area with poor hygiene scores, high hygiene scores, highly rated restaurants, using filtering and aggregation techniques.
   
## Conclusions 
 1. Most unhygenic restaurants: 41 count
 2. Highest rated restaurants in London Area: 33 count
 3. Highest rated restaurants in a 0.01 Long/Lat radius of Penang Flavours: 87
 
 #### Areas with the cleanest restaurants (Top 5)
 | LocalAuthorityName | count      |
 |--------------------|------------|
 | Thanet             | 1130       |
 | Greenwich          | 882        |
 | Maidstone          | 713        |
 | Newham             | 711        |
 | Swale              | 686        |


## Plots
None for this challenge.

## Resources
None.

## Licences 
This code has no license restrictions. Challenge files are provided by the Columbia School of Engineering.
