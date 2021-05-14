from bs4 import BeautifulSoup
import requests
import time
from random import randint
import re
import pandas as pd

url = 'https://www.retrogames.co.uk/Site_Map.html'

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}

# product url's
links = []
inventory = []

counter = 1

# loop to generate product url's
for li in soup.find('ul', class_='prodItems'):
    for link in li:
        links.append('https://www.retrogames.co.uk/' + link['href'])
for i in links:

    r = requests.get(i, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')

    title = soup.find('span', class_='pagetitles').text.strip()
    price = soup.find('span', class_='ourprice').text.strip().replace('£ ', '')

    try:
        stock = soup.find('font', color='009900').text.strip().split(':')[0]
    except:
        stock = 'Out of stock'

    image = [img['href'] for img in soup.find_all('a', id='thumb1')][0]
    image_url = f'https://www.retrogames.co.uk/{image}'
    desc = soup.find('meta', {'name': 'description'}).get('content')
    product_url = i
    #test_url = 'https://www.retrogames.co.uk/007521/Sinclair/3D-Tunnel-by-New-Generation'
    platformregex = re.compile(r'(http[s]?:)?([^\s]+\d{6}/)([A-Za-z]*)(/.*)')
    platform_search = platformregex.match(product_url)
    if platform_search:
        platform = platform_search.group(3)


    data = {
        'Title': title,
        'Price': price,
        'Stock': stock,
        'Image_url': image_url,
        'Description': desc,
        'Product_url': product_url,
        'Platform': platform
        }
    inventory.append(data)
    print(f'Saving: {data} : {counter} of {len(links)}')
    counter = counter + 1

    time.sleep(0.5)

df = pd.DataFrame(inventory)
df.to_csv('retro_games.csv')
