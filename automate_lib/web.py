from random import choice
import newspaper
from newspaper import Article
from keyboard import *

news_urls = [
    {'url': 'http://www.indiatimes.com', 'lg': 'en'},
    {'url': 'http://www.bild.de/', 'lg': 'de'},
    {'url': 'http://www.thesun.co.uk/', 'lg': 'en'},
    {'url': 'https://www.nytimes.com/', 'lg': 'en'},
    {'url': 'http://cnn.com', 'lg': 'en'},
    {'url': 'http://www.xinhuanet.com', 'lg': 'zh'},
    {'url': 'http://www.aguilardigital.es/', 'lg': 'es'},
]


def scrapy_content_newsurl():
    article_urls = []
    news_url = choice(news_urls)
    print('news url: {}'.format(news_url['url']))
    
    news_paper = newspaper.build(news_url['url'])
    
    try:
        for article in news_paper.articles:
            print('article url: {}'.format(article.url))
            article_urls.append(article.url)
        
        try_count = 0
        while True:
            if try_count > len(article_urls):
                scrapy_content_newsurl()
            
            else:
                print('article urls: {}'.format(len(article_urls)))
                url = article_urls[random.randint(0, len(article_urls) - 1)]
                if news_url['lg'] != 'en':
                    a = Article(url, language=news_url['lg'])
                else:
                    a = Article(url)

    
    except Exception as e:
        print('Exception: {}'.format(e))
        scrapy_content_newsurl()


if __name__ == '__main__':
    content = scrapy_content_newsurl()
    print('content: {}'.format(content))