from bs4 import BeautifulSoup
import requests

# url = 'https://www.retrogames.co.uk/Site_Map.html'
#
# r = requests.get(url)
# soup = BeautifulSoup(r.content, 'html.parser')
#
# # product url's
# links = []
#
# # loop to generate product url's
# for li in soup.find('ul', class_='prodItems'):
#     for link in li:
#         links.append('https://www.retrogames.co.uk/' + link['href'])

testurl = 'https://www.retrogames.co.uk/007760/Sinclair/Dustman-by-Timescape'
out_stock = 'https://www.retrogames.co.uk/000346/Atari/Ace-of-Aces-by-Atari'

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

format = soup.find_all(class_='mainheaders')

for i in format:
    for text in i:
        print(text)  # todo need to extarct text from list