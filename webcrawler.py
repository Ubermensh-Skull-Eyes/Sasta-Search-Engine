# Importing Libraries

import requests
import sys
import lxml
from bs4 import BeautifulSoup
import string

# Creating Access URL

url = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_area'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}
try:
    Web = requests.get(url,headers=headers)
except requests.exceptions.RequestException as e:
    print(f"Error occured :{e}")
    sys.exit(1)

# Creating a Soup Object

Soup = BeautifulSoup(Web.content,'lxml')

# File Extraction

Table = Soup.find_all('table')[1]
Country = Table.find_all('a')
Country_links = [link['href'] for link in Country]


# Clean the list

Country_links = [a for a in Country_links if not a.startswith('#')]



links = []
for a in Country_links:
    urls = 'https://en.wikipedia.org'+ a
    links.append(urls)

# Input from User

Search = input("Enter a Country Name:- ")
Search = Search.replace(' ','_')
count = 1

for i in links:
    Flag = False
    if Search.upper() in i.upper():
        try:
            Country_f = requests.get(i,headers=headers)
        except requests.exceptions.RequestException as e : 
            print(f"Failed :{e}")
        Country_Soup =  BeautifulSoup(Country_f.content,'lxml')
        Country_Content = Country_Soup.find_all('p')[1]
        print(count)
        print('URL:'+i)
        print("Country Info:"+Country_Content.text.strip())
        count = count+1
if count ==1:
    print("No element Found")
