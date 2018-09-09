# import dependencies
import bs4
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
# from selenium import webdriver
# from lxml import html
import csv
from datetime import datetime, date, timedelta
from pytz import timezone
import pandas as pd


# url of ucsc college 9 & 10 dining hall
url = 'https://nutrition.sa.ucsc.edu/nutframe.asp?sName=UC+Santa+Cruz+Dining&locationNum=40&locationName=Colleges+Nine+%26+Ten+Dining+Hall&naFlag=1'


# scrap the menu data from the webpage
# since the menu data is cannot be scrapped from the html file directly
# we have to make additional requests to get the frame page contents 
with requests.Session() as session:
    response = session.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    for frame in soup.select("frameset frame"):
        frame_url = urljoin(url, frame["src"])
        response = session.get(frame_url)
        frame_soup = BeautifulSoup(response.content, 'html.parser') 
        # print(frame_soup.prettify())


# extract both the meal name and food name from html
meal_name = frame_soup.find_all('div', attrs={'class': 'menusampmeals'})
food_name = frame_soup.find_all('div', attrs={'class': 'menusamprecipes'})


# convert the name of the meal type in html form to a list form
meal_type = [item.string for item in meal_name]
print('Length: ', len(meal_type))
for i in meal_type:
    print(i)
print()
print('-' * 40 + '\n')

# convert the food name in html form to a list form
food_list = [item.string for item in food_name]
print('Food list length: ', len(food_list))
for food in food_list:
    print(food)
print()
print('-' * 40 + '\n')

# In case of dupliate food name, the list should be converted to a set
# sort
food_list = sorted(list(set(food_list)))
print('Sorted length: ', len(food_list))
for food in food_list:
    print(food)
print()
print('-' * 40 + '\n')

# preference list, labeled by myself
# pref_1 = [1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0 ]
# pref_2 = [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0]
pref_3 = [0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1]


# timezone setting
us_pacific = timezone('US/Pacific')
time = datetime.now(us_pacific)
us_time = time.strftime('%Y-%m-%d')
print('Current US/Pacific time: ', us_time)
print()


# write the food list to a csv file
path = '/Users/7w0r4ng3s/Desktop/menu_scraping/{}.csv'.format(us_time)
print('Current path: ', path)
print()


def write_csv():
    with open(path, "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        for key, val in zip(food_list, pref_3):
            writer.writerow([key, val])
    print('write_csv: COMPLETED')

    df = pd.read_csv('{}.csv'.format(us_time), names=['food', 'pref'])
    df.to_csv('{}.csv'.format(us_time))
    print('add_column_name: COMPLETED')

    


if __name__ == "__main__":
	write_csv()
