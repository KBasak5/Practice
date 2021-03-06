# -*- coding: utf-8 -*-
"""Webscraping2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hSD-KWj3VyLmLVzNBRUTDgMv-hh8LiYb
"""

import requests

wikilink = "https://en.wikipedia.org/wiki/List_of_Asian_countries_by_area"
link = requests.get(wikilink).text

link1 = requests.get(wikilink)
link1

type(link)

requests.models.Response?

print(link)

# To display it in pretty manner we use BeautifulSoup

from bs4 import BeautifulSoup
soup = BeautifulSoup(link,'lxml')  # BeautifulSoup using xml parser   lxml since html uses lexical xml format
# now Html object is created

print(soup.prettify())   # This will give us formatted html back,  we will be getting which is under what

print(soup.title)  # prints the first occurance of title

print(soup.title.string)

print(soup.a)

print(soup.find_all("a"))

list1 = []
for link_1 in soup.find_all('a'):
  list1.append(link_1.get('href'))        # get function is used to get the specified attribute

print(list1)

for ref in list1:
  print(ref)

"""Now we will scrap the table from the web page.
For this we need to go the developers tool of that page and determine our target table.
The details we got from web page will be stored in an excel file. 
"""

final_table = soup.find('table',class_ = "wikitable")

final_table

lst_rows = final_table.find_all('tr')
lst_rows

country = []
area = []
for row in lst_rows:
  lst_td = row.find_all('td')
  if len(lst_td) > 1:
    a_tag = lst_td[1].find('a')
    if a_tag is not None:
      country.append(a_tag.get('title'))
      area.append(lst_td[2].text.rstrip())   # strip() removes leading and trailing white spaces [lstrip() -- only leading, rstrip()-- only trailing]

print(len(country))
print(len(area))

print(country)
print(area)

import pandas as pd
df = pd.DataFrame({"Country":country,"Area":area})
df

df.to_excel("output_Webscraping2.xlsx",index=False)

