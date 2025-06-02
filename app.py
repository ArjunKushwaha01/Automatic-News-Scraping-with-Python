from flask import Flask, render_template, request, redirect, url_for, flash, session
import feedparser
import newspaper
import os
import uuid
import time

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'default_dev_key')

# Simulated user database (for demo)
users = {}

# In-memory article cache
article_cache = {}
cache_timestamp = 0
CACHE_EXPIRY = 300  # 5 minutes

def scrape_news_from_feed(feed_url):
    global article_cache, cache_timestamp

    if time.time() - cache_timestamp < CACHE_EXPIRY:
        return list(article_cache.values())

    articles = []
    feed = feedparser.parse(feed_url)
    new_cache = {}

    for entry in feed.entries:
        try:
            article = newspaper.Article(entry.link)
            article.download()
            article.parse()
            article_id = str(uuid.uuid4())
            full_article = {
                'id': article_id,
                'title': article.title or entry.get('title', ''),
                'author': ', '.join(article.authors) if article.authors else entry.get('author', 'Unknown'),
                'publish_date': str(article.publish_date) if article.publish_date else entry.get('published', ''),
                'content': article.text or entry.get('summary', '')
            }
            new_cache[article_id] = full_article
            articles.append(full_article)
        except Exception as e:
            print(f"Failed to process article: {entry.link}\nError: {e}")

    article_cache.clear()
    article_cache.update(new_cache)
    cache_timestamp = time.time()
    return articles

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/home')
def home():
    if 'username' not in session:
        flash('Please log in to access the homepage.', 'warning')
        return redirect(url_for('login'))
    articles = scrape_news_from_feed('http://feeds.bbci.co.uk/news/rss.xml')
    return render_template('home.html', articles=articles)

@app.route('/article/<article_id>')
def article_detail(article_id):
    article = article_cache.get(article_id)
    if not article:
        flash("Article not found.", "danger")
        return redirect(url_for('home'))
    return render_template('article.html', article=article)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid credentials. Please try again.', 'danger')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            flash('Username already exists. Please choose a different one.', 'danger')
        else:
            users[username] = password
            flash('Registration successful! You can now log in.', 'success')
            return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash("You have been logged out.", "info")
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run()
