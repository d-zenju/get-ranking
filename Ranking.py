# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup

"""
class Yahoo
- Get Yahoo Shopping Category Ranking
- http://developer.yahoo.co.jp/webapi/shopping/shopping/v1/categoryranking.html
"""
class Yahoo:
    # Request URL (XML)
    xmlUrl = 'http://shopping.yahooapis.jp/ShoppingWebService/V1/categoryRanking'

    # init
    def __init__(self, appid):
        self.appid = appid  # appid : Your's application ID (required)
        self.url = self.xmlUrl + '?appid=' + self.appid
<<<<<<< HEAD

=======
        
>>>>>>> 63ec4b6335163cddf8289012cca30e963bf40a16
    # make request URL
    '''
    input : params(dict), output : url(string)
    "params" conforms to request parameters of Yahoo Shipping API
    '''
    def requestUrl(self, params):
        if 'output' in params:
            self.url += '&output=' + params['output']
        if 'affiliate_type' in params:
            self.url += '&affiliate_type=' + params['affiliate_type']
        if 'affiliate_id' in params:
            self.url += '&affiliate_id=' + params['affiliate_id']
        if 'callback' in params:
            self.url += '&callback=' + params['callback']
        if 'category_id' in params:
            self.url += '&category_id=' + params['category_id']
        if 'gender' in params:
            self.url += '&gender=' + params['gender']
        if 'generation' in params:
            self.url += '&generation=' + params['generation']
        if 'period' in params:
            self.url += '&period=' + params['period']
        if 'offset' in params:
            self.url += '&offset=' + params['offset']
        if 'type' in params:
            self.url += '&type=' + params['type']
            
    def getXML(self):
        xml = urllib2.urlopen(self.url)
        soup = BeautifulSoup(xml, 'lxml')
        print soup


class Rakuten:
    def __init__(self):
        pass


class Amazon:
    def __init__(self):
        pass