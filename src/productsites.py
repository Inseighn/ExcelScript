import requests
import json
from bs4 import BeautifulSoup
import config

class Newegg:
    def get(id):
        _headers = {
            'User-Agent' : 'Newegg AndroidTablet App / 4.0.4'
        }
        _link = "http://www.ows.newegg.com/Products.egg/{}/Detail?"
        response = None
        response = requests.get(_link.format(id), proxies=config.proxies, headers=_headers)

        if not response:
            if __debug__:
                print ("Null Response.")
            return ''

        json_data = response.json()
        if not json_data:
            if __debug__:
                print ("Error generating JSON data.")
            return ''

        if ('Basic' in json_data) and ('FinalPrice' in json_data['Basic']):
            price = json_data['Basic']['FinalPrice']
            if price == '':
                return json_data['Basic']['AddToCartText']
            else:
                if(price.find("$") == 0):
                    return price[price.index("$") + 1:]
                else:
                    return price
        else:
            if __debug__:
                print("Basic/FinalPrice keys not found in json response.")
            return '';
class CDW:
    def get(link):
        response = None
        response = requests.get(link, proxies=config.proxies)
        if not response:
            if __debug__:
                print ("Error getting page information.")
            return ''
        soup = BeautifulSoup(response.text, "html.parser")
        spans = soup.findAll("span", attrs={'itemprop' : 'price',})
        if spans:
            if spans[0].text:
                return spans[0].text
            else:
                print (spans)
                return spans[0].text
        else:
            if __debug__:
                print (spans)
            return ''
class PCON:
    def get(link):
        response = None
        response = requests.get(link, proxies=config.proxies)
        if not response:
            if __debug__:
                print ("Error getting page information")
            return "Invalid Link."
        soup = BeautifulSoup(response.text, "html.parser")
        scripts = soup.findAll("script")
        for script in scripts:
            if "product_price" in script.text:
                json_string = json.loads(script.text[script.text.index("{"):script.text.index("}")+1])
                if json_string and ('product_price' in json_string):
                    return json_string['product_price']
                else:
                    return json_string
        if "we found no matches" in soup.text:
            return "Invalid Link"
        return ""
class PCM:
    def get(link):
        response = None
        response = requests.get(link, proxies=config.proxies)
        if not response:
            return ""
        soup = BeautifulSoup(response.text, "html.parser")
        divs = soup.findAll("div", "total-price-con")
        if divs:
            price = divs[0].text
            if "$" in price:
                return price[price.index("$")+1:]
            return price
        return ""
class Insight:
    def get(id):
        json_data = {
            'searchText': [id],
            'defaultPlant': '10',
            'loadAccessories': 'false',
            'cartFlag': 'false',
            'fromcs': 'false',
            'loadRecommendedProducts': 'true',
            'salesOrg': '2400',
            'user': {},
            'locale': 'en_us',
            'softwareContractIds': [],
            'similarMaterialId': id,
            'contractId': None,
        }
        header = {
            'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36',
            'X-Requested-With' : 'XMLHttpRequest',
            'Content-Type' : 'application/json',
            'Accept' : 'application/json',
        }
        link = "https://www.insight.com/insightweb/getProductInfo"
        response = None
        response = requests.post(link, json=json_data, proxies=config.proxies, headers=header)
        if not response:
            return ""
        json_response = response.json()
        if(json_response and ('webProduct' in json_response)):
            price = json_response['webProduct']['prices'][0]['price']
            return price
        return ""
class Zones:
    def get(link):
        response = None
        response = requests.get(link, proxies=config.proxies)
        if not response:
            return ""
        soup = BeautifulSoup(response.text, "html.parser")
        spans = soup.findAll("span", "prod-price")
        if spans:
            price = spans[0].text
            if "$" in price:
                return price[price.index("$") + 1:]
            return price
        return ""
class Prov:
    def get(id):
        link = "http://www.provantage.com/scripts/cart.dll/feed6b1/V{}"
        response = None
        response = requests.get(link.format(id), proxies=config.proxies)
        if not response:
            return ""
        if id in response.text:
            arr = response.text[response.text.index("(") + 1:response.text.index(")")].replace("\'", "").split(",")
            if len(arr) >= 3:
                return arr[3]
        return ""
