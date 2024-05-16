#!/usr/bin/env python3
import requests
from urllib.request import Request, urlopen
import os
from bs4 import BeautifulSoup

def get_url_paths(url, ext='', params={}):
    authorization= os.environ['MAVEN_AUTH']
    request = Request(url)
    request.add_header('Authorization', authorization)
    response = urlopen(request)
    response_text = response.read()
    soup = BeautifulSoup(response_text, 'html.parser')
    parent = [url + node.get('href') for node in soup.find_all('a') if not node.get('href').endswith('../')]
    return parent

url = 'https://maven.jacoti.com/artifactory/snapshot/com/jacoti/'
ext = ''
result = get_url_paths(url, ext)
for artifact in result:
    versions= get_url_paths(artifact,ext)
    for version in versions:
        if not version.endswith('/'):
            continue
        parts= version.split('/')
        print( "com.jacoti:%s:%s" % (parts[-3],parts[-2])) 

