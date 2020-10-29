import urllib.request

from bs4 import BeautifulSoup

url = 'https://www.youtube.com/'

page_html = None

try: 
    page = urllib.request.urlopen(url)
    page_html = page.read()
    page.close()

except:
    print('failed')

# at this point 
bsoup_page = BeautifulSoup(page_html, features='html.parser')

print(type(bsoup_page))

# id='video-title-link'