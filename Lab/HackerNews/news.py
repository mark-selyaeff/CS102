import requests
from bs4 import BeautifulSoup
from pprint import pprint as pp
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def get_news(text):
    page = BeautifulSoup(text, 'html.parser')
    news_page = page.body.center.table.findAll('tr')[3].td.table.findAll('tr')
    articles = []
    for i in range(0, len(news_page), 3):
        try:
            news_header_td = news_page[i].findAll('td')[2]
            news_author_td = news_page[i + 1].findAll('td')[1]
            title = news_header_td.find('a').text
            author = news_author_td.findAll('a')[0].text
            try: # Проверка на наличие ссылки
                link = news_header_td.span.a.span.text
            except AttributeError:
                link = None
            try: # Проверка на наличие комментариев
                comments = int(news_author_td.findAll('a')[-1].text.split()[0])
            except ValueError:
                comments = 0
            try: # Проверка на наличие очков
                points = int(news_author_td.findAll('span')[0].text.split()[0])
            except ValueError:
                points = 0
            article = {'title': title, 'author': author, 'url': link, 'comments': comments, 'points': points}
            articles.append(article)
        except IndexError:
            continue
    return articles


r = requests.get("https://news.ycombinator.com/news?p=3")
news = get_news(r.text)

Base = declarative_base()

class News(Base):
    __tablename__ = "news"
    id = Column(Integer, primary_key = True)
    title = Column(String)
    author = Column(String)
    url = Column(String)
    comments = Column(Integer)
    points = Column(Integer)
    label = Column(String)

engine = create_engine("sqlite:///news.db")
Base.metadata.create_all(bind=engine)
session = sessionmaker(bind=engine)
s = session()

# for article in news:   # Adding news to DB
#     n = News(**article)
#     s.add(n)
#     s.commit()

from bottle import route, run, template

@route('/')
@route('/hello/<name>')
def index(name="Stranger"):
    return template('hello_template', name=name)

run(host='localhost', port=8080)


