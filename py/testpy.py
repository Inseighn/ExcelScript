import requests
import config
import json
import os
from pathlib import Path
from bs4 import BeautifulSoup
from requests import Session


def testLink(link):
    r = requests.get(link, proxies=config.proxies)
    soup = BeautifulSoup(r.content)
    index1 = r.text.find('(') + 1
    index2 = r.text.find(')')
    arr = r.text[index1:index2].replace('\'','')
    print (arr.split(',')[3])
if __name__ == "__main__":
    testLink("http://www.provantage.com/scripts/cart.dll/feed6b1/VNECJ044")
