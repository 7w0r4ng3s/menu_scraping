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
from collections import defaultdict


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
print(meal_type)

# convert the food name in html form to a list form
food_list = [item.string for item in food_name]
print(food_list)


# preference list, labeled by myself
# pref_1 = [1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0 ]
pref_2 = [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0]

# timezone setting
us_pacific = timezone('US/Pacific')
time = datetime.now(us_pacific)
us_time = time.strftime('%Y-%m-%d')


# write the food list to a csv file
csv_path = '/Users/7w0r4ng3s/Desktop/menu_scraping/{}.csv'.format(us_time)


# def write_full():
#     with open(csv_path, "w") as output:
#         writer = csv.writer(output, lineterminator='\n')
#         for key, val in zip(food_list, pref_2):
#             writer.writerow([key, val])
# write_full()

def write_food():
    with open(csv_path, 'w') as output:
        writer = csv.writer(output, lineterminator='\n')
        for food in food_list:
            writer.writerow([food])
write_food()

# read the csv file of the current day
# the dataframe will be compared with the 0th row (food list) of the full data and extract those
# which 
df_today = pd.read_csv('{}.csv'.format(us_time), header=None)
df_prev = pd.read_csv('{}.csv'.format(prev_date), header=None)

# select the first column of both days, type = series
prev_col = df_prev.iloc[:, 0]
today_col = df_today.iloc[:, 0]

# extract the intersection of both menus and convert it to a list
intersec = pd.Series(list(set(today_col).intersection(set(prev_col))))
intersec = intersec.tolist()


# create a dict of preference for previous day
col_2 = df_prev.iloc[:, 1].tolist()
col_1 = prev_col.tolist()
dict_prev = dict(zip(col_1, col_2))

today_list = today_col.tolist()

default_pref = [0] * len(today_list)
pref_list_today = []
# today_dict = dict
# for food in intersec:
#     if food in dict_prev.keys():





