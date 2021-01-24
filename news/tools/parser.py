import os
from typing import List

import requests
import pymysql
from datetime import datetime
from dotenv import load_dotenv


# path to .env file
dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


def get_items_id() -> List[int]:
    """Function for get list with new's id from HackerNews

    Returns:
        List with new's id

    """
    url = 'https://hacker-news.firebaseio.com/v0/newstories/.json'
    req = requests.get(url)

    items_id = req.json()

    return items_id


def get_news(items_id: List[int]) -> List[dict]:
    """Function for get list with news

    Args:
        items_id: List with new's id

    Returns:
        List with news

    """
    news = []

    for item in items_id:
        url = f'https://hacker-news.firebaseio.com/v0/item/{item}.json'
        req = requests.get(url)
        data = req.json()

        if 'title' in data and 'url' in data:
            new = dict(title=data['title'], url=data['url'], created=datetime.now())
            news.append(new)

        if len(news) == 30:
            break

    return news


def save_news(news: List[dict]) -> None:
    """Function for save data to DB

    Args:
        news: List with news

    Returns:
        None

    """

    connection = pymysql.connect(host=os.environ['HOST_DB'],
                                 user=os.environ['USER_DB'],
                                 password=os.environ['PASSWORD_DB'],
                                 database=os.environ['NAME_DB'],
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    with connection.cursor() as cursor:
        # Create a new record
        for new in news:
            sql = "INSERT INTO news_news (title, url, created) VALUES (%s, %s, %s)"
            date = datetime.now()
            cursor.execute(sql, (new['title'], new['url'], date))

    connection.commit()


def main():
    items_id = get_items_id()
    news = get_news(items_id)
    save_news(news)
