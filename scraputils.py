import requests
from bs4 import BeautifulSoup


def extract_news(parser):
    """ Extract news from a given web page """
    news_list = []
    news=parser.table.findAll('table')[1]
    i=0
    while i<90:
        title=news.findAll('tr')[i].findAll('td')[2].find('a').text #тайтл
        name=news.findAll('tr')[i+1].findAll('td')[1].find('a').text #имя
        upvotes=news.findAll('tr')[i+1].findAll('td')[1].find('span').text #апвоты
        comments=news.findAll('tr')[i+1].findAll('td')[1].findAll('a')[-1].text #комменты
        if len(news.findAll('tr')[i].findAll('td')[2].findAll('a'))==2:
            url=news.findAll('tr')[i].findAll('td')[2].findAll('a')[0]["href"] #ссылка
        else:
            url='Ссылки нет'
        if comments=='discuss':
            comments="0 comments"
        comments=comments.replace('\xa0',' ')
        news_list.append({'title':title,'author':name,'points':upvotes,'comments':comments,'url':url})
        i+=3
    return news_list

def extract_next_page(parser):
    """ Extract next page URL """
    news=parser.table.findAll('table')[1]
    return news.findAll('tr')[-1].findAll('td')[1].find('a')['href']

def get_news(url, n_pages=1):
    """ Collect news from a given web page """
    news = []
    while n_pages:
        print("Collecting data from page: {}".format(url))
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html5lib")
        news_list = extract_news(soup)
        next_page = extract_next_page(soup)
        url = "https://news.ycombinator.com/" + next_page
        news.extend(news_list)
        n_pages -= 1
    return news



