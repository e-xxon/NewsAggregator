from bottle import (
    route, run, template, request, redirect
)
import string
import time
from bs4 import BeautifulSoup
import requests
from scraputils import get_news,extract_next_page
from db import News, session
from bayes import NaiveBayesClassifier,clean


@route("/news")
def news_list():
    s = session()
    rows = s.query(News).filter(News.label == None).all()
    return template('news_template', rows=rows)


@route("/add_label/")
def add_label():
    label = request.query.label
    id = int(request.query.id)
    s=session()
    news = s.query(News).filter(News.id==id).one()
    news.label=label
    s.add(news)
    s.commit()
    redirect("/news")


@route("/update")
def update_news():
    url='https://news.ycombinator.com/newest'
    A=True
    s=session()
    titles=s.query(News.title).all()
    while A:
        newnews=get_news(url)
        for thing in newnews:
            if thing["title"] not in titles:
                s.add(News(**thing))
            else:
                A=False
        time.sleep(2)
        response=requests.get(url)
        page=BeautifulSoup(response.text, "html5lib")
        nextpage=extract_next_page(page)
        url='https://news.ycombinator.com/'+nextpage
    s.commit()
    redirect("/news")


@route("/classify")
def classify_news():
    s=session()
    X_fit,y_fit,X_test=[],[],[]
    fitnews=s.query(News).filter(News.label != None).all()
    testnews=s.query(News).filter(News.label == None).all()
    for one in fitnews:
        X_fit.append(one.title)
        y_fit.append(one.label)
    for two in testnews:
        X_test.append(two.title)
    model=NaiveBayesClassifier()
    model.fit(X_fit,y_fit)
    labels=model.predict(X_test)
    rows=zip(testnews,labels)
    return template('classify_template', rows=rows)

if __name__ == "__main__":
    run(host="localhost", port=8080)

