import requests
from bs4 import BeautifulSoup
from pprint import pprint as pp
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from bottle import redirect
# for training ->
from collections import defaultdict
from math import log
from nltk.stem.lancaster import LancasterStemmer

# NLTK -> Stem это модуль для обработки морфологии в словах

classes, freq = defaultdict(lambda:0), defaultdict(lambda:0) # P(C), P(O|C)
labels = {'good': 1, 'maybe': 2, 'never': 3}

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


r = requests.get("https://news.ycombinator.com/news?p=1")
news = get_news(r.text)

Base = declarative_base()

def classify(title):
    st = LancasterStemmer()
    result = min(classes.keys(), key = lambda cl: -log(classes[cl]) + \
            sum(-log(freq.get((cl, st.stem(word)), 10**(-7))) for word in title.split() ))
    return result

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

from bottle import route, run, template, request

@route('/')
@route('/hello/<name>')
def index(name="Stranger"):
    return template('hello_template', name=name)

@route('/news')
def news_list():
    s = session()
    rows = s.query(News).filter(News.label == None).all()
    rows_good = [x for x in rows if classify(x.title)=='good']
    rows_maybe = [x for x in rows if classify(x.title)=='maybe']
    rows_never = [x for x in rows if classify(x.title)=='never']
    return template('news_template', rows_good=rows_good, rows_maybe=rows_maybe, rows_never=rows_never)

@route('/add_label')
def add_label():
    s = session()
    label = request.query.label
    id = request.query.id

    article = s.query(News).filter(News.id == int(id)).first()
    article.label = label
    s.commit()
    # 1. Получить значения параметров label и id из GET-запроса
    # 2. Получить запись из БД с соответствующим id (такая запись только одна!)
    # 3. Изменить значение метки записи на значение label
    # 4. Сохранить результат в БД
    redirect('/news')

@route('/update_news')
def update_news():
    # 1. Получить данные с новостного сайта
    # 2. Проверить каких новостей еще нет в БД. Будем считать,
    #    что каждая новость может быть уникально идентифицирована
    #    по совокупности двух значений: заголовка и автора
    # 3. Сохранить в БД те новости, которых там нет
    s = session()
    site = requests.get("https://news.ycombinator.com/news?p=2")
    new_news = get_news(site.text)
    for article in new_news:
        if not s.query(News).filter(News.title == article['title'] and News.author == article['author']).all():
            n = News(**article)
            s.add(n)
            s.commit()
    redirect('/news')

@route('/train')
def train():
    global classes, freq
    classes, freq = defaultdict(lambda: 0), defaultdict(lambda: 0)
    st = LancasterStemmer()
    s = session()
    labeled_articles = s.query(News).filter(News.label != None).all()
    for article in labeled_articles:
        classes[article.label] += 1
        words = article.title.split()
        for word in words:
            freq[article.label, st.stem(word)] += 1

    for label, word in freq:
        freq[label, word] /= classes[label]
    for c in classes:
        classes[c] /= len(labeled_articles)
    redirect('/news')


run(host='localhost', port=8080)


