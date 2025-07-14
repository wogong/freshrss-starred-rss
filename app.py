import xml.etree.ElementTree as ET
from flask import Flask, Response
import time
import os
from dotenv import load_dotenv
from freshrss import FreshRss

load_dotenv()

config = {
    'freshrss_url': os.environ.get('FRESHRSS_URL'),
    'freshrss_username': os.environ.get('FRESHRSS_USERNAME'),
    'freshrss_api_password': os.environ.get('FRESHRSS_API_PASSWORD'),
}
print("DEBUG: config =", config)  # 添加此行

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
        #ET.SubElement(entry, 'description').text = item.get('summary', {}).get('content', '')
        ET.SubElement(entry, 'description').text = 'remove full text for personal usage.'
        ET.SubElement(entry, 'pubDate').text = time.strftime('%a, %d %b %Y %H:%M:%S +0000', time.gmtime(item['published']))

    return ET.tostring(rss, encoding='unicode')

@app.route('/starred.xml')
def serve_rss():
    items = get_starred_items()
    rss_content = generate_rss(items)
    return Response(rss_content, mimetype='application/rss+xml')



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
