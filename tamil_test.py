import feedparser
from bs4 import BeautifulSoup

from urllib.parse import urlparse

def get_domain_from_url(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    return domain

# Function to fetch RSS feed data
def get_tamil_rss_feed_data(url, num_posts=10):
    feed = feedparser.parse(url)
    data = []
    counter = 0
    # news_website_name = feed.feed.title 
    for entry in feed.entries:
        if counter >= num_posts:
            break
        
        title = entry.title
        description = entry.description
        pub_date = entry.published
        content_html = entry.content[0].value
        content_text = BeautifulSoup(content_html, 'html.parser').get_text()
        source_url = entry.link 
        news_website_name = get_domain_from_url(source_url)


        image_url = None
        
        # Extract the image URL from the content if available
        content_soup = BeautifulSoup(content_html, 'html.parser')
        image_element = content_soup.find('img')
        if image_element:
            image_url = image_element['src']
        
        data.append({
            'title': title,
            'summary': description,
            'published_date': pub_date,
            'content': content_text,
            'image_url': image_url,
            'source_url' : source_url,
            'source_name' :  news_website_name
        })
        
        counter += 1

    return data


def tamil_feeds(url_list, num_posts=20):
    combined_data = []
    for url in url_list:
        feed_data = get_tamil_rss_feed_data(url, num_posts)
        combined_data.extend(feed_data)
    combined_data.sort(key=lambda x: x['published_date'], reverse=True)
    return combined_data





# # Example usage
# # url = 'http://feeds.feedburner.com/Hindu_Tamil_india.xml'
# # feed_data = get_rss_feed_data(url, num_posts=5)

# # # Print the extracted data
# for post in feed_data:
#     print('Title:', post['title'])
#     print('Description:', post['description'])
#     print('Published Date:', post['published_date'])
#     print('Content:', post['content'])
#     print('Image URL:', post['image_url'])
#     print('---')