# Food Preference Project

> It is a prototype project of generatng different food reports of the dining hall in my school.

## Overview

The project uses web scraping to scrape data from the dining hall website. The data consists of food names and perference defined by myself (0 for dislike and 1 for like). All the data are in CSV format and the data of the new day will be appended to the full dataset, which is Data.csv. 

So far it can search the whole dataset if I give it a name of a certain food or even a keyword (part of the name). It will show you how many times the food appears and how many times you like the food.

Functionalities will be continuously added in the future.

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
