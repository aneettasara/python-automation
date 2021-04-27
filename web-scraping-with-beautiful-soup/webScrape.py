import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
#print(soup) # HTML - Source Code

quotes = soup.find_all('span',class_='text')
authors = soup.find_all('small',class_='author')
tags = soup.find_all('div',class_='tags')
#print(quotes) # List of Quotes

for i in range(len(quotes)):
    print(quotes[i].text)
    print(authors[i].text)
    quoteTag = tags[i].find_all('a',class_='tag')
    for eachTag in quoteTag:
        print(eachTag.text)
    print()
