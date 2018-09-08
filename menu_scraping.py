
# import dependencies
import bs4
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
# from selenium import webdriver
# from lxml import html
import csv
import datetime
from pytz import timezone


# ---------- Get request from the webpage and extract food name ----------

# url of ucsc college 9 & 10 dining hall
url = 'https://nxxutrition.sa.ucsc.edu/nutframe.asp?sName=UC+Santa+Cruz+Dining&locationNum=40&locationName=Colleges+Nine+%26+Ten+Dining+Hall&naFlag=1'

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


# ---------- Convert the original format to a list of food names ----------
# The list meal_type may be used in the future

# convert the name of the meal type in html form to a list form
# meal_type = [item.string for item in meal_name]
# print(meal_type)

# convert the food name in html form to a list form
food_list = [item.string for item in food_name]
print(food_list)


# preference list, labeled by myself (like or dislike)
pref_2 = [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0]


# ---------- Make a csv files containing food list and preference ----------

# timezone setting (title of the csv file)
us_pacific = timezone('US/Pacific')
time = datetime.now(us_pacific)
us_time = time.strftime('%Y-%m-%d')

# write the food list to a csv file
csv_path = '/Users/7w0r4ng3s/Desktop/menu_scraping/{}.csv'.format(us_time)

with open(csv_path, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for key, val in zip(food_list, pref):
        writer.writerow([key, val])    