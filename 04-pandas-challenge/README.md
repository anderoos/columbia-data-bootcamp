# CU-4-Pandas-Challenge

## Description
In this challenge project, we are tasked with observing trends to help a fictional school board and mayor make strategic decisions regarding future school budgeting and priorities. We are given a csv file containing students, schools within the district, math and reading scores, school type and budget.
## Approach and Analysis
Using pandas library in python,  I grouped students based on schools and calculated the mean value of math and reading scores based on school name, school type, and budgets.
The mean value of math and reading scores were used as a metric to assess overall school performance. The mean value was then used to calculate overall passing score. In this instance, the passing score were students that scored above 70% in both math and reading.
## Conclusions
### District Summaries
![alt text](https://github.com/anderoos/CU-4-pandas-challenge/blob/main/PyCitySchools/Images/Screenshot%202023-09-13%20at%2010.39.02%E2%80%AFAM.png)
![alt text](https://github.com/anderoos/CU-4-pandas-challenge/blob/main/PyCitySchools/Images/Screenshot%202023-09-12%20at%208.42.03%E2%80%AFPM.png)
### Of the fifteen schools in this city:
* Charter schools tend to perform better than district schools
  * Charter schools perform better than district schools

![alt text](https://github.com/anderoos/CU-4-pandas-challenge/blob/main/PyCitySchools/Images/Screenshot%202023-09-12%20at%208.40.44%E2%80%AFPM.png)
* Budget has a strong inverse effect on performance
  * When looking at the allocated budget per capita, schools with a higher budget per student perform worse than schools with lower budgets per student.
  * Lowest performing schools had a budget over $650 per student
  * Highest performing schools had a budget below $635 per student

![alt text](https://github.com/anderoos/CU-4-pandas-challenge/blob/main/PyCitySchools/Images/Screenshot%202023-09-12%20at%208.41.21%E2%80%AFPM.png)
* Student population plays a strong role in student performance
  * The top 5 performing schools had a student population of less than 2500 students
  * The bottom 5 performing schools had a student population of more than 2900 students, with the worst performing school having the largest student population of 4761 students

![alt text](https://github.com/anderoos/CU-4-pandas-challenge/blob/main/PyCitySchools/Images/Screenshot%202023-09-13%20at%2011.16.22%E2%80%AFAM.png)
![alt text](https://github.com/anderoos/CU-4-pandas-challenge/blob/main/PyCitySchools/Images/Screenshot%202023-09-12%20at%208.41.12%E2%80%AFPM.png)
![alt text](https://github.com/anderoos/CU-4-pandas-challenge/blob/main/PyCitySchools/Images/Screenshot%202023-09-12%20at%208.41.55%E2%80%AFPM.png)
![alt text](https://github.com/anderoos/CU-4-pandas-challenge/blob/main/PyCitySchools/Images/Screenshot%202023-09-12%20at%208.41.48%E2%80%AFPM.png)
## Limitations and recommendations
* Budget: I recommend cutting student budgets for schools with a budget per student of above $600. Although budget shows an inverse effect relationship with performance, it does not show *how* each school is spends their budget; whether they spend their budget extracurricular activities like school events or student resources, teachers and technologies that may boost performance metrics.
* School sizes: recommend cutting school sizes to no more than 2500 students. 
## Resources
None
## Licensing
This code has no license restrictions. Challenge files are provided by the Columbia School of Engineering.
