pip install requests
import pandas as pd
from bs4 import BeautifulSoup
import requests
req_headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
}
questionlist = []

req2_headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
}

def getQuestions(page):
    with requests.Session() as s:
      url = 'https://www.zillow.com/champaign-il/rentals/?searchQueryState=%7B%22mapBounds%22%3A%7B%22west%22%3A-88.83466886914063%2C%22east%22%3A-87.75526213085938%2C%22south%22%3A39.82291721457712%2C%22north%22%3A40.43966618489985%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A4042%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22category%22%3A%22cat2%22%2C%22pagination%22%3A%7B%7D%7D'
      r = s.get(url, headers=req_headers)
      soup = BeautifulSoup(r.content, 'html')
      jobs=soup.find_all('article',class_='list-card list-card-additional-attribution list-card_not-saved')
      for item in jobs:
        question = {
            'address': item.find('address', {'class': 'list-card-addr'}).text,
            'price': item.find('div', {'class': 'list-card-price'}).text.replace('$','').replace('/mo','').replace(',','').replace('+',''),
            'beds':item.find('li', {'class': ''}).text.replace('bds','').replace('bd','').replace('to','-').replace('Studio','1'),
            'site':'Zillow',
            'posted': item.find('div', {'class': 'list-card-variable-text list-card-img-overlay'}).text.replace('on Zillow','ago').replace('Updated yesterday','Recently Updated'),
            'area':'Champaign'
        }
        questionlist.append(question)
      return

for x in range(1,50):
    getQuestions(x)

df = pd.DataFrame(questionlist)
def getQuestions1(page):
    with requests.Session() as s:
      url = 'https://www.apartments.com/champaign-il/'
      r = s.get(url, headers=req_headers)
      soup = BeautifulSoup(r.content, 'html')
      jobs1=soup.find_all('li',class_='mortar-wrapper')
      for item in jobs1:
        question1 = {
            'address': item.find('a', {'class': 'property-link'}).text.replace(',','').replace('\n',''),
            'price': item.find('div', {'class': 'price-range'}).text.replace('$','').replace('/mo','').replace(',',''),
            'beds': item.find('div', {'class': 'bed-range'}).text.replace('Bed','').replace('to','-').replace('Studio',''),
            'site':'Apartments.com',
            'posted': item.find('span', {'class': 'listingFreshness'}).text.replace('\n\n','').replace('\n','').replace('hrs','hours').replace('days','day').replace('wk','week').replace('wks','week'),
        }
        questionlist.append(question1)
      return

for x in range(1,10):
    getQuestions1(x)

df1 = pd.DataFrame(questionlist)
def getQuestions2(page):
    with requests.Session() as s:
      url = 'https://hotpads.com/champaign-il/apartments-for-rent'
      r = s.get(url, headers=req2_headers)
      soup = BeautifulSoup(r.content, 'html')
      jobs2=soup.find_all('li',class_='ListingWrapper')
      for item in jobs2:
        question2 = {
            'address': item.find('h4', {'class':'styles__ListingCardName-y78yl0-8 jQmZHq'}).text.replace('\n',''),
            'price': item.find('div', {'class': 'styles__ListingCardPrice-y78yl0-17 cguwHc'}).text.replace('$','').replace(',','').replace('+',''),
            'beds': item.find('div', {'class': 'styles__ListingCardBedDisplay-y78yl0-7 iPqMa'}).text.replace('beds','').replace('bed','').replace('to','-').replace('Studio',''),
            'site':'Hotpads.com',
            'posted': 'Recently Updated',
            'area':'Champaign'
            
        }
        questionlist.append(question2)
      return

for x in range(1,11):
    getQuestions2(x)

df2 = pd.DataFrame(questionlist)

df2.columns=['Address','Price','Beds','Website','Posted','Area']
df2['Area']=df2['Address'].apply(lambda x: 'Urbana' if 'urbana' in x.lower() else 'Champaign')
df2['Minimum_Beds']=df2['Beds'].apply(lambda x:x.split('-')[0])
df2['Maximum_Beds']=df2['Beds'].apply(lambda x:x.split('-')[-1])
df2['Minimum_Cost']=df2['Price'].apply(lambda x:x.split('-')[0])
df2['Maximum_Cost']=df2['Price'].apply(lambda x:x.split('-')[-1])
df2['Minimum_Cost'] = pd.to_numeric(df2['Minimum_Cost'])
df2['Maximum_Cost'] = pd.to_numeric(df2['Maximum_Cost'])
df2['Average_Cost']=(df2['Minimum_Cost']+df2['Maximum_Cost'])/2
df2.drop('Address', axis=1, inplace=True)
from sklearn import preprocessing
label_encoder = preprocessing.LabelEncoder()
  
# Encode labels in column 'species'.
df2['Website']= label_encoder.fit_transform(df2['Website'])
  
df2['Website'].unique()
df2['Area']= label_encoder.fit_transform(df2['Area'])
df2['Area'].unique()
df2['Posted']= label_encoder.fit_transform(df2['Posted'])
df2['Posted'].unique()
df2['Maximum_Beds']= label_encoder.fit_transform(df2['Maximum_Beds'])
df2['Maximum_Beds'].unique()
df2['Minimum_Beds']= label_encoder.fit_transform(df2['Minimum_Beds'])
df2['Minimum_Beds'].unique()
df2.drop('Price', axis=1, inplace=True)
df2.drop('Beds', axis=1, inplace=True)
df2['Minimum_Beds'] = pd.to_numeric(df2['Minimum_Beds'])
df2['Maximum_Beds'] = pd.to_numeric(df2['Maximum_Beds'])
df2['Website'] = pd.to_numeric(df2['Website'])
df2['Posted'] = pd.to_numeric(df2['Posted'])
df2['Area'] = pd.to_numeric(df2['Area'])
df2['Average_Cost'] = pd.to_numeric(df2['Average_Cost'])
import numpy as np

from scipy.stats import uniform, randint

from sklearn.datasets import load_breast_cancer, load_diabetes, load_wine
from sklearn.metrics import auc, accuracy_score, confusion_matrix, mean_squared_error
from sklearn.model_selection import cross_val_score, GridSearchCV, KFold, RandomizedSearchCV, train_test_split

import xgboost as xgb


X = df2.iloc[:, :5].values
y = df2.iloc[:, -1].values

xgb_model = xgb.XGBRegressor(objective="reg:linear", random_state=42)

xgb_model.fit(X, y)

y_pred = xgb_model.predict([[1,15,0,7,4]])
print(y_pred)
