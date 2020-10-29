from urllib import request, error

from bs4 import BeautifulSoup

url = 'https://www.wuxiaworld.com/novels'

page_html = None
page = None


page = request.urlopen(url)
page_html = page.read()
page.close()



# at this point 
bsoup_page = BeautifulSoup(page_html, features='html.parser')

# print(bsoup_page.prettify())

# Grabbing element entities
# Grabbing All of a Type
print(type(bsoup_page))

# By ID:
# bsoup_page.find(id='id_name')

# Goal to find a website, then actually scrape a category