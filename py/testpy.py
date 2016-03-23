import requests
import config
import json
import os
from pathlib import Path
from bs4 import BeautifulSoup
from requests import Session


def testLink(link):
    print (str(Path(__file__).parent.parent) + config.ExcelFile)

if __name__ == "__main__":
    testLink("http://www.pcconnection.com/product/lacie-250gb-porsche-design-slim-drive-p-9223-usb-3.0-portable-solid-state-drive/9000515/17677878")
