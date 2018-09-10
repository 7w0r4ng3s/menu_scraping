# Food Preference Project Using Machine Learning

> The project is a food preference recommender which using the menu data from UCSC dining hall and labels on different foods to recommend the food I like. Since the project is currently still in development, some functionalities is waiting to be completed in the future.

## Overview

The first part of the project is completed. It uses web scraping (html) techniques to scrape data from [UCSC College 9 & 10 Dining Hall](https://nutrition.sa.ucsc.edu/nutframe.asp?sName=UC+Santa+Cruz+Dining&locationNum=40&locationName=Colleges+Nine+%26+Ten+Dining+Hall&naFlag=1). After the data is scraped, the program will drop the duplicate foods in a single day and makes it a food list sorted in alphabetical order.

For each day's food, I will provide the program with a list of preference, which is a list of numbers consiting of 0 (dislike) and 1 (like). The data collecting process will be conducted once per 24 hours after the web page updates the menu.

Then the labeled data will be written to a csv file with a name of the current date (i.e. 2018-09-10.csv). After the data for every single day, the csv file will also be append to 'Data.csv', which includes all the food names and labels (with duplicates).

## Installation

Dependencies

* os
* bs4 (BeautifulSoup)
* requests
* urllib.parse (urljoin)
* csv
* datetime
* pandas

Install dependencies with `pip`

## Usage

Run `python3 scraping.py`
