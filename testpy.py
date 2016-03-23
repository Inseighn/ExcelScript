import requests
import config
import json
from bs4 import BeautifulSoup
from requests import Session


def testLink(link):
    r = requests.get(link, proxies=config.proxies)
    if not r:
        return 0
    soup = BeautifulSoup(r.content)
    spans = soup.find_all('script')
    index1 = spans[2].string.index('{')
    index2 = spans[2].string.index('}') + 1
    json_string = spans[2].string[index1:index2]
    json_string = json.loads(json_string)
    print (json_string['product_price'])

if __name__ == "__main__":
    testLink("http://www.pcconnection.com/product/lacie-250gb-porsche-design-slim-drive-p-9223-usb-3.0-portable-solid-state-drive/9000515/17677878")
