import feedparser
from bs4 import BeautifulSoup


def tamil_feed_data(url, num_posts=10):
    feed = feedparser.parse(url)
    data = []
    counter = 0
    news_website_name = feed.feed.title 
        
    for entry in feed.entries:
        if counter >= num_posts:
            break
        title = entry.title
        pub_date = entry.published
        summary_html = entry.summary
        summary_text = BeautifulSoup(summary_html, 'html.parser').get_text()
        source_url = entry.link 

        # Extract the image URL from the content
        content_html = entry.content[0]['value']
        content_soup = BeautifulSoup(content_html, 'html.parser')
        image_url = content_soup.find('img')['src']

        data.append({
            'title': title,
            'published_date': pub_date,
            'summary': summary_text,
            'source_url': source_url,
            'image_url': image_url
        })
        counter += 1
    return data