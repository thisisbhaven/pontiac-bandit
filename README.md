# MilkBasketHackathon
BPM2 is a static recommendation system made using Bayesian Popularity Ranking which would be dynamic on supplying real time data
Recency is an RFM analysis table giving customer ids in priority to provide offers to
Persuade is an RFM analysis table giving customer ids to persuade for a subscription
cust_all provides a comprehensive RFM analysis for the user to derive insights
There is a product to product recommender in the notebook, about which is mentioned in the last cell
There is an LSTM Model in the notebook for time series analysis which could not be trained due to lack of GPU resources.ee
Comprehensive graphs for RFM analysis available in the notebook

## Python Django Backend App deployment -
Install django on your local machine
Install dependencies
Cd milkbasket
run - python manage.py runserver
This will live the APIs

## React Native App deployment
Cd mbapp
Change base url in React Native app
Install dependencies
run - expo start
