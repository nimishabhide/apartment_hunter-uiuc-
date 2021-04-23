!pip install autoscraper
import pandas as pd
from autoscraper import AutoScraper
questionlist=[]
scraper = AutoScraper()
url = 'https://www.apartmentfinder.com/Illinois/Champaign-Apartments'
wanted_list = ["1806 S Cottage Grove Ave, Urbana, IL 61801","$665 - $895","2 - 4 Beds","ApartmentFinder","1 Day Ago","Urbana"]
result = scraper.build(url, wanted_list)
scraper.get_result_similar("https://www.apartmentfinder.com/Illinois/Champaign-Apartments",grouped=True)
scraper.set_rule_aliases({'rule_8kkl': 'Address', 'rule_r50f': 'Price','rule_2op6':'Beds','rule_q444':'Posted','rule_4zff':'Area'})
scraper.keep_rules(['rule_8kkl', 'rule_r50f','rule_2op6','rule_q444','rule_4zff'])
scraper.save('github-repository-search')
scraper.load('github-repository-search')
result=scraper.get_result_similar("https://www.apartmentfinder.com/Illinois/Champaign-Apartments/",group_by_alias=True)
d1=pd.DataFrame(result)
result1=scraper.get_result_similar("https://www.apartmentfinder.com/Illinois/Champaign-Apartments/Page5",group_by_alias=True)
d2=pd.DataFrame(result1)
d1=d1.append(d2)
print(d1)
