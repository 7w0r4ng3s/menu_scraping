# import dependencies
import os
import bs4
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
# from selenium import webdriver
# from lxml import html
import csv
from datetime import datetime
from pytz import timezone
import pandas as pd
import tools


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
# pref_3 = [0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1]
# pref_4 = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0]
# pref_5 = [1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0]
pref = []
for i in food_list:
    print(i)
    preference = int(input())
    pref.append(preference)
print(pref)
len('Preference length: ', pref)

# timezone setting
us_pacific = timezone('US/Pacific')
time = datetime.now(us_pacific)
us_time = time.strftime('%Y-%m-%d')
print('Current US/Pacific time: ', us_time)
print()


# write the food list to a csv file
path = '/Users/7w0r4ng3s/Desktop/menu_scraping/data/{}.csv'.format(us_time)
print('Current path: ', path)
path_2 = '/Users/7w0r4ng3s/Desktop/menu_scraping/data/'
print()


def write_data():
    # Write today's menu to a csv file containing food list and preference
    with open(path, "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        for key, val in zip(food_list, pref):
            writer.writerow([key, val])
    print('write_csv: COMPLETED')
    # add index and column names
    df = pd.read_csv(path, names=['food', 'pref'])
    df.index.names = ['index']
    df.to_csv(path)
    print('add_column_name: COMPLETED')

# def merge_data():
#     # TODO: Figure out a way to get rid of the unnamed: 0 column
#     # TODO: Modify merge_data() so that new data can be append to data.csv
#     files = [f for f in os.listdir('.') if os.path.isfile(f)]
#     merged = []
#     for f in files:
#         filename, ext = os.path.splitext(f)
#         if ext == '.csv':
#             read = pd.read_csv(f)
#             merged.append(read)

#     result = pd.concat(merged)
#     result.to_csv('data.csv')
    # perform additional steps to get rid of those extra columns

def append_data():
    df1 = pd.read_csv('Data.csv', index_col='index')
    df1.index.names = ['index']
    df2 = pd.read_csv(path, index_col='index')
    df3 = df1.append(df2).reset_index()
    df3 = df3.drop('index', 1).sort_values('food').reset_index().drop('index', 1)
    df3.index.names = ['index']
    df3.to_csv('Data.csv')


if __name__ == "__main__":
    write_data()
    append_data()
