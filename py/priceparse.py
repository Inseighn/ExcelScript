import requests
import config
import json
from bs4 import BeautifulSoup
from requests import Session

def get_price(link, name):
    if name.lower() == "newegg":
        return get_newegg_price(link)
    elif name.lower() == "cdw":
        return get_cdw_price(link)
    elif name.lower() == "pc connections":
        return get_pcon_price(link)
    elif name.lower() == "pcm":
        return get_pcm_price(link)
    elif name.lower() == "insight":
        return get_insight_price(link)
    elif name.lower() == "zones":
        return get_zones_price(link)
    else:
        return "123"

def get_newegg_price(link):
    headers = {
    'User-Agent' : 'Newegg AndroidTablet App / 4.0.4'
    }
    r = requests.get("http://www.ows.newegg.com/Products.egg/" + link + "/Detail?", proxies=config.proxies, headers=headers)
    json_data = r.json()
    if json_data:
        return json_data['Basic']['FinalPrice']
    else:
        return ""

def get_cdw_price(link):
    r = requests.get(link, proxies=config.proxies)
    soup = BeautifulSoup(r.content)
    spans = soup.find_all("span", attrs={'itemprop' : 'price',})
    if spans:
        return (spans[0].string)
    else:
        return 0

def get_pcon_price(link):
    r = requests.get(link, proxies=config.proxies)
    if not r:
        return 0
    soup = BeautifulSoup(r.content)
    spans = soup.find_all('script')
    index1 = spans[2].string.index('{')
    index2 = spans[2].string.index('}') + 1
    json_string = spans[2].string[index1:index2]
    json_string = json.loads(json_string)
    return (json_string['product_price'])

def get_pcm_price(link):
    r = requests.get(link, proxies=config.proxies)
    if not r:
        return 0
    soup = BeautifulSoup(r.content)
    divs = soup.find_all('div', 'total-price-con')
    if divs:
        return divs[0].string
    else:
        return 0

def get_insight_price(link):
    json_data = {
        'searchText': [link],
        'defaultPlant': '10',
        'loadAccessories': 'false',
        'cartFlag': 'false',
        'fromcs': 'false',
        'loadRecommendedProducts': 'true',
        'salesOrg': '2400',
        'user': {},
        'locale': 'en_us',
        'softwareContractIds': [],
        'similarMaterialId': link,
        'contractId': None,
    }

    header = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36',
        'X-Requested-With' : 'XMLHttpRequest',
        'Content-Type' : 'application/json',
        'Accept' : 'application/json',
    }

    res = requests.post('https://www.insight.com/insightweb/getProductInfo', json=json_data, proxies=config.proxies, headers=header)
    json_response = res.json()
    return (json_response['webProduct']['prices'][0]['price'])

def get_zones_price(link):
    r = requests.get(link, proxies=config.proxies)
    if not r:
        return 0
    soup = BeautifulSoup(r.content)
    spans = soup.find_all('span', 'prod-price')
    return (spans[0].string)
