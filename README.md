# 336-Data-Essays
Source files used to collect and analyze data for 
Polsci 336 (Energy Politics, Prof. Brian Min) at The University of Michigan. 

### Essay Text:

Essay #1: ELECTRICITY USE, WEALTH, AND DEMOCRACY (9/23/2017)

_On Collecting and Visualizing Data:_ To begin this assignment, I used the World Bank Data API to collect information on 
GDP per Capita Figures, as well a Electricity use per Capita. Data for each is strong up to 2014, after which there are 
missing entries for a variety of countries. In order to assemble the most complete data sets, I chose to use the year 
2014 as my focus. The data pulled from the World Bank was cleaned and parsed first into python dictionaries, then into 
DataFrame objects using Pandas. Data on Democratic Level was sourced from the Center for Systemic Peace INSCR Data Page, 
using the "Polity2" score for each nation. Using the Electricity Use data as a control set, the Dem Level and GDP sets 
were trimmed to match.     

_**-- in progress -- 
Completion expected on or before September 23rd, 2017**_