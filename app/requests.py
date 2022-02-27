from sre_parse import CATEGORIES
from unicodedata import category, name
from app import app,models
import urllib.request,json
from .models import news

News = news.News


def get_news(category):
    '''
    Function that gets json reponse to url request
    '''
    news_api_url = app.config['NEWS_API_URL']
    apiKey = app.config['NEWS_APIKEY']
    get_news_url = news_api_url.format(category, apiKey)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)

    return news_results


def process_results(news_list):
    '''
    Function thay process the news result and transform them to a list of obejects
    Args: 
        news_list: a list of dictionaries that contain news details
    Returns:
        news_results: a list of news objects
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        country = news_item.get('country')
        
        if description:
            news_object = News(id, name, description, url, category, country)
            news_results.append(news_object)

    return news_results

