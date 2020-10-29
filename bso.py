import urllib.request

from bs4 import BeautifulSoup

url = 'https://www.amazon.com/b?node=283155'
# page = urllib.request.urlopen('https://www.amazon.com/b?node=283155')
page = ''
try: 
    page = urllib.request.urlopen(url)
    print(page)
except:
    print('failed')
    print(page)