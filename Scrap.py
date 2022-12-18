#Taiyo Assignment by Sourav De


from selenium import webdriver
import pandas as pd
website = 'https://opentender.eu/start'

driver = webdriver.Chrome()
driver.get("https://opentender.eu/start")
country_data = driver.find_elements_by_xpath('//*[@id="app"]/start/div[2]/div/div[2]/ul/li')


country_list = []

value_list = []
value1 = [] 
for data in country_data:
    value1.append(data.text)


for i in value1:
    country,value = i.split("\n")
    country_list.append(country)
    value_list.append(value)

# print(country_list)
# print(value_list)

df = pd.DataFrame({'country': country_list , 'No of tenders':value_list})
df.to_csv('data.csv', index=False)
print(df)

