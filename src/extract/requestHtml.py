__author__ = 'aahammer'

import requests
from lxml import html, etree

def getHTMLPageAsXML(url, proxy, timeout=60):

    r = requests.get(url, proxies=proxy, timeout = timeout)
    tree = html.fromstring(r.text)
    return tree

def getDummyHTML():
    with open('C:/Users/aahammer/Desktop/d.html', 'r') as file:
        tree = html.fromstring(file.read())
        file.close
    return tree

