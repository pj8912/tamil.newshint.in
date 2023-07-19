from flask import Flask, redirect, render_template, send_from_directory, request, url_for, make_response
import os
from dotenv import load_dotenv
load_dotenv()
from combined import *
from tamil_test import * 
from tm_live_updates import *
# from flask_sitemapper import Sitemapper
from dynamic_sitemap import SimpleSitemap, ChangeFreq
from datetime import datetime
from urllib.parse import urlparse
import pytz




app = Flask(__name__,  static_folder='static')
app.config["UPLOAD_FOLDER"] = "static"
app.use_static_route = True




#home
@app.route('/')
def tamil_home():
    rss_urls = ['https://rss.app/feeds/_e8ITHRwacULSBlOw.xml']
    feed_data = combine_feeds(rss_urls, num_posts=10)
    return render_template('tm.html', data=feed_data)


@app.route('/top')
def tamil_top():
    rss_urls = ['https://tamil.news18.com/rss/live-updates.xml']
    feed_data = tm_live_feeds(rss_urls, num_posts=25)
    return render_template('tm-top.html', data=feed_data)
 
@app.route('/india')
def tamil_india():
    rss_urls = ['https://feeds.feedburner.com/Hindu_Tamil_india.xml']
    feed_data = tamil_feeds(rss_urls, num_posts=25)
    return render_template('tm-india.html', data=feed_data)


# http://feeds.feedburner.com/Hindu_Tamil_business
@app.route('/business')
def tamil_business():
    # rss_urls = [' http://feeds.feedburner.com/Hindu_Tamil_business.xml','https://rss.app/feeds/_q41GWepEG8mNeHJ6.xml']
    rss_urls = ['https://rss.app/feeds/_q41GWepEG8mNeHJ6.xml']
    feed_data = combine_feeds(rss_urls, num_posts=25)
    return render_template('tm-business.html', data=feed_data)


@app.route('/sports')
def tamil_sports():
    # rss_urls = ['http://feeds.feedburner.com/Hindu_Tamil_sports.xml','https://rss.app/feeds/_k2rqiIeSPSyaOO6Q.xml']
    rss_urls = ['https://rss.app/feeds/_k2rqiIeSPSyaOO6Q.xml']
    feed_data = combine_feeds(rss_urls, num_posts=25)
    return render_template('tm-sports.html', data=feed_data)


# http://feeds.feedburner.com/Hindu_Tamil_world

@app.route('/world')
def tamil_world():
    rss_urls = ['https://rss.app/feeds/_MdfoYWnwjAxKbABX.xml']
    feed_data = combine_feeds(rss_urls, num_posts=25)
    return render_template('tm-world.html', data=feed_data)


@app.route('/tech')
def tamil_tech():
    # rss_urls = ['https://feeds.feedburner.com/Hindu_Tamil_technology.xml']
    rss_urls = ['https://rss.app/feeds/_ZeQaG5gCo2OeTdZi.xml']
    feed_data = combine_feeds(rss_urls, num_posts=25)
    return render_template('tm-tech.html', data=feed_data)


# ---------------------------------------tamil entertainment-------------------------------------
@app.route('/entertainment')
def tamil_cinema():
    rss_urls = ['http://feeds.feedburner.com/Hindu_Tamil_cinema.xml','https://rss.app/feeds/_p0h70aFAPUUGKRSK.xml']
    feed_data = combine_feeds(rss_urls, num_posts=15)
    return render_template('tm-cinema.htm', data=feed_data)


# ---------------------------------------tamil politics-------------------------------------

@app.route('/politics')
def tm_politics():
    rss_urls = ['https://rss.app/feeds/_PmtcEvLWGCljeeTv.xml']
    feed_data = combine_feeds(rss_urls, num_posts=25)
    return render_template('tm-politics.html', data=feed_data)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/terms-and-conditions')
def tnc():
    return render_template('tnc.html')

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')


@app.route("/sitemap")
@app.route("/sitemap/")
@app.route("/sitemap.xml")
def sitemap():
    host_components = urlparse(request.host_url)
    host_base = host_components.scheme + "://" + host_components.netloc

    static_urls = [
        {"loc": f"{host_base}/terms-and-conditions"},
        {"loc": f"{host_base}/about"},
        {"loc": f"{host_base}/privacy"},

    ]
    # Dynamic routes with dynamic content
    dynamic_urls = []
    d_urls = [
        f"{host_base}/",
        f"{host_base}/sports",
        f"{host_base}/entertainment",
        f"{host_base}/top",
        f"{host_base}/politics",
        f"{host_base}/world",
        f"{host_base}/business",
        f"{host_base}/technology",
        ]
     
    for i in d_urls:
        url = {
            "loc" : i,
            "priority" : "0.9",
        }
        dynamic_urls.append(url)    

    xml_sitemap = render_template("sitemap.xml", static_urls=static_urls, dynamic_urls=dynamic_urls)
    response = make_response(xml_sitemap)
    response.headers["Content-Type"] = "application/xml"

    return response


if __name__ == "__main__":
    app.run(debug=True,port=7000) 



