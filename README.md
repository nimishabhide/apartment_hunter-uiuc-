# apartment_hunter-uiuc-
This is my first ever end to end project which would be more of a research as I will be using different kind of web scrappinf mechanisms, regression models for prediction and I would be making use of AWS for storage of data and in the end using visuaizayion tools.
I made this project to scrape data from different websites for apartments and help understand the price range one should be looking out for finding an apartment near UIUC.
Used websites like Zillow,apartments.com and hotpads to scrape data for evaluation.
I have also used a new way for scrapping data off https://www.apartmentfinder.com/Illinois/Champaign-Apartments/ using autoscraper library na have included a code(renter.py) for that as well but I personally prefer the traditional method as you have to keep changing the rule_id of columns every time you run the program. Hence it makes it way less usable compared to the original approach.
Have uploaded clean data and numeric data csv files which were used for this evaluation. 
Used this website to find the best regressor that fits the data-https://regclass.herokuapp.com/
Have used both multiple regressor and XGBoost for prediction.
I have used two different styles for using regressor.
The XGBoost algorithm turns out to be the best.
I have put the cleaned data into AWS RDS(MySQL) and have also included the code for it(ws_rent_illinois). I then extracted the collected data to the Tableau platform where I did visualization for the same. The images of the visualization are attached below.

KPI(Key Performance Indicator)
The average cost of apartments in illinois is around $1100.4526315789474 as per the data collected so for measuring the KPI, use the following: avg=1100.45
KPI= ((Cost of the apartment - avg)/avg) x 100
If the percentage that you are getting is a positive value, you are making an excellent deal others, you should consider better options or negotiate.


