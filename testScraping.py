# -*- coding: utf-8 -*-
"""
Created on Thu May 30 20:29:43 2019

@author: tanuj
"""

# =============================================================================
# import requests 
# URL = "https://www.geeksforgeeks.org/data-structures/"
# r = requests.get(URL) 
# print(r.content) 
# =============================================================================


# =============================================================================
# import requests
# from bs4 import BeautifulSoup 
# 
# URL = "http://www.values.com/inspirational-quotes"
# r = requests.get(URL) 
# 
# soup = BeautifulSoup(r.content, 'html.parser') 
# print(soup.prettify()) 
# =============================================================================

#Python program to scrape website 
#and save quotes from website 
import requests 
from bs4 import BeautifulSoup 
import csv 

URL = "http://www.values.com/inspirational-quotes"
r = requests.get(URL) 

soup = BeautifulSoup(r.content, 'html5lib') 

quotes=[] # a list to store quotes 

table = soup.find('div', attrs = {'id':'portfolio'}) 
#print(table.prettify())
for row in table.findAll('article', attrs = {'class':'portfolio-item quotation appreciation'}): 
	quote = {} 
	quote['img'] = row.img['src'] 
	quote['lines'] = row.img['alt'] 
	quotes.append(quote) 

print(quotes)
filename = 'inspirational_quotes.csv'
with open(filename, 'w') as f: 
	w = csv.DictWriter(f,['img','lines']) 
	w.writeheader() 
	for quote in quotes: 
		w.writerow(quote) 

# importing csv module 
import csv 

# initializing the titles and rows list 
fields = [] 
rows = [] 

# reading csv file 
with open(filename, 'r') as csvfile: 
	# creating a csv reader object 
	csvreader = csv.reader(csvfile) 
	
	# extracting field names through first row 
	fields = next(csvreader) 

	# extracting each data row one by one 
	for row in csvreader: 
		rows.append(row) 

	# get total number of rows 
	print("Total no. of rows: %d"%(csvreader.line_num)) 

# printing the field names 
print('Field names are:' + ', '.join(field for field in fields)) 

# printing first 5 rows 
print('\nFirst 5 rows are:\n') 
for row in rows[:5]: 
	# parsing each column of a row 
	for col in row: 
		print("%10s"%col), 
	print('\n') 


