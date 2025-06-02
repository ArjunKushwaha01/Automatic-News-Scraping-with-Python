# scraper.py
from datetime import datetime
import feedparser
import newspaper

def scrape_news_from_feed(feed_url):
    articles = []
    feed = feedparser.parse(feed_url)
    for entry in feed.entries:
        try:
            article = newspaper.Article(entry.link)
            article.download()
            article.parse()
            articles.append({
                'title': article.title or entry.get('title', ''),
                'author': ', '.join(article.authors) or entry.get('author', ''),
                'publish_date': str(article.publish_date) or entry.get('published', ''),
                'content': article.text or entry.get('summary', ''),
                'link': entry.link
            })
        except Exception as e:
            print(f"Failed to process article: {entry.link}\nError: {e}")
    return articles


def scrape_news_from_feed(feed_url):
    articles = []
    feed = feedparser.parse(feed_url)
    for entry in feed.entries:
        try:
            article = newspaper.Article(entry.link)
            article.download()
            article.parse()
            
            # Format publish date nicely
            publish_date = None
            if article.publish_date:
                publish_date = article.publish_date.strftime('%b %d, %Y %H:%M %p')
            elif entry.get('published'):
                try:
                    # Parse entry.published (string) to datetime and format it
                    parsed_date = datetime(*entry.published_parsed[:6])
                    publish_date = parsed_date.strftime('%b %d, %Y %H:%M %p')
                except Exception:
                    publish_date = entry.get('published', '')
            
            articles.append({
                'title': article.title or entry.get('title', ''),
                'author': ', '.join(article.authors) or entry.get('author', ''),
                'publish_date': publish_date or '',
                'content': article.text or entry.get('summary', ''),
                'link': entry.link
            })
        except Exception as e:
            print(f"Failed to process article: {entry.link}\nError: {e}")
    return articles
