from bs4 import BeautifulSoup
import requests
import time
from random import randint
import re

url = 'https://www.retrogames.co.uk/Site_Map.html'

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

# product url's
links = []
inventory = []

counter = 1

# loop to generate product url's
# for li in soup.find('ul', class_='prodItems'):
#     for link in li:
#         links.append('https://www.retrogames.co.uk/' + link['href'])
# for i in links:

testurl = 'https://www.retrogames.co.uk/007760/Sinclair/Dustman-by-Timescape'
# out_stock = 'https://www.retrogames.co.uk/000346/Atari/Ace-of-Aces-by-Atari'

r = requests.get(testurl)
soup = BeautifulSoup(r.content, 'html.parser')

title = soup.find('span', class_='pagetitles').text.strip()
price = soup.find('span', class_='ourprice').text.strip()

try:
    stock = soup.find('font', color='009900').text.strip().split(':')[0]
except:
    stock = 'Out of stock'

image = [img['href'] for img in soup.find_all('a', id='thumb1')][0]
image_url = f'https://www.retrogames.co.uk/{image}'
desc = soup.find('meta', {'name': 'description'}).get('content')
product_url = i

platformregex = r"(http[s]?:\/\/)?([^\/\s]+\/\d\d\d\d\d\d\/)([A-Za-z]*)(.*)"  # match will be group 3
platform =

data = {
    'Title': title,
    'Price': price,
    'Stock': stock,
    'Image_url': image_url,
    'Description': desc,
    'Product_url': product_url
    }
inventory.append(data)
print(f'Saving: {data} : {counter} of {len(links)}')
counter = counter + 1

time.sleep(randint(1, 3))



