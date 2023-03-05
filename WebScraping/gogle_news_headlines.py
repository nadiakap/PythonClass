import requests
import re


def get_headlines(rss_url):
    """
    @returns a list of titles from the rss feed located at `rss_url`    
    """
    try:
        
        response = requests.get(rss_url)
        title_regex = "<title>(.+?)</title>"
        pattern = re.compile(title_regex)   
        return re.findall(pattern,response.text)
    
    except:
        
        print('smth went wrong...')
        return 
    
google_news_url="https://news.google.com/news/rss"
print(get_headlines(google_news_url))
