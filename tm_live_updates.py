import feedparser
from bs4 import BeautifulSoup

# Function to fetch RSS feed data
def tm_live_rss_feed_data(url, num_posts=50):
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

        # Fetch image URL from description
        description_html = entry.description
        description_soup = BeautifulSoup(description_html, 'html.parser')
        image_url = description_soup.find('img')['src'] if description_soup.find('img') else None

        data.append({
            'title': title,
            'published_date': pub_date,
            'summary': summary_text,
            'source_url': source_url,
            'image_url': image_url,
            'source_name' :  news_website_name
        })
        counter += 1
    return data

# Example usage
# rss_url = "https://tamil.news18.com/rss/live-updates.xml"
def tm_live_feeds(url_list, num_posts=20):
    combined_data = []
    for url in url_list:
        feed_data = tm_live_rss_feed_data(url, num_posts)
        combined_data.extend(feed_data)
    combined_data.sort(key=lambda x: x['published_date'], reverse=True)
    return combined_data
