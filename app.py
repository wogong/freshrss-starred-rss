import xml.etree.ElementTree as ET
from flask import Flask, Response
import schedule
import time
from freshrss import FreshRss
from helpers import read_config_file
config = read_config_file()

app = Flask(__name__)

def get_starred_items():
    freshrss = FreshRss(config['freshrss_url'], config['freshrss_username'], config['freshrss_api_password'],)
    freshrss.get_auth_token()
    starred = freshrss.get_starred()['items']
    return starred

def generate_rss(items):
    rss = ET.Element('rss', version='2.0')
    channel = ET.SubElement(rss, 'channel')
    ET.SubElement(channel, 'title').text = 'FreshRSS Starred Items'
    ET.SubElement(channel, 'link').text = config['freshrss_url']
    ET.SubElement(channel, 'description').text = 'Starred items from FreshRSS'

    for item in items:
        entry = ET.SubElement(channel, 'item')
        ET.SubElement(entry, 'title').text = item['title']
        ET.SubElement(entry, 'link').text = item['alternate'][0]['href']
        ET.SubElement(entry, 'description').text = item.get('summary', {}).get('content', '')
        ET.SubElement(entry, 'pubDate').text = time.strftime('%a, %d %b %Y %H:%M:%S +0000', time.gmtime(item['published']))

    return ET.tostring(rss, encoding='unicode')

@app.route('/starred.xml')
def serve_rss():
    items = get_starred_items()
    rss_content = generate_rss(items)
    return Response(rss_content, mimetype='application/rss+xml')

def update_rss():
    print("Updating RSS feed...")
    items = get_starred_items()
    rss_content = generate_rss(items)
    with open('starred.xml', 'w', encoding='utf-8') as f:
        f.write(rss_content)

if __name__ == '__main__':
    schedule.every(12).hours.do(update_rss)
    update_rss()  # initial update
    app.run(host='0.0.0.0', port=5000)
