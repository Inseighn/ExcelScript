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
    spans = soup.find_all("b")
    print (len(spans))
    for span in spans:
        print (span)

if __name__ == "__main__":
    testLink("http://www.provantage.com/nec-display-solutions-np-m282x~7NECJ044.htm")
