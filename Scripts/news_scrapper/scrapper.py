import requests
from bs4 import BeautifulSoup
import time
import os
import json


def get_url_2(root, link):
    if len(link) > 8:
        if link[:8] == 'https://':
            url_2 = str(link)
        else:
            url_2 = str(url) + str(link)
    else:
        url_2 = str(url) + str(link)

    return url_2

def run_scrapper(site, q, **kwargs):

    if site == 'in_q':
        url = q
    elif site == 'bing':
        url = 'https://www.bing.com/news/search?q={0}'.format(q)
    else:
        url = 'https://www.ecosia.org/search?q={0}'.format(q)

    response = requests.get(url)
    scrap = {}

    if response.ok:
        soup = BeautifulSoup(response.text, features='html.parser')

        if site == 'bing':
            articles = soup.findAll('div', {'class': 'news-card'})
            scrap['size'] = len(articles)

            scrap['articles'] = {}
            for i in range(len(articles)):
                article = articles[i]

                title = article.find('a', {'class': 'title'}).text
                link = article.find('a', {'class': 'title'}).get('href', None)

                scrap['articles'][i] = {
                    'title': title,
                    'link': link,
                }
        if site == 'in_q':
            title = soup.find('title').text
            description = soup.find('p').text

            scrap = {
                'title': title,
                'description': description,
            }

    return scrap


scrap = run_scrapper('bing', 'art+strasbourg')

for i in range(scrap['size']):
    url = scrap['articles'][i]['link']
    response = requests.get(url)

    scrap['articles'][i]['scrap'] = run_scrapper('in_q', url)

for key, article in scrap['articles'].items():
    print('\n*******\n\ttitle : {0}\ndescription : {1}\nlink : {2}'.format(article['title'], article['scrap']['description'], article['link']))

timestamp = int(time.time())
scrap['date'] = timestamp


dir_path = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(dir_path, 'scrap_{0}.txt'.format(str(timestamp))), 'a') as file:
    file.write(json.dumps(scrap, indent=4))
