# -*- coding: utf-8 -*-

import time
import datetime
import urllib2
from bs4 import BeautifulSoup
import bottlenose
import sqlite3

"""
class Yahoo
- Get Yahoo Shopping Category Ranking
- http://developer.yahoo.co.jp/webapi/shopping/shopping/v1/categoryranking.html
"""
class Yahoo:
    # Request URL (XML)
    xmlUrl = 'http://shopping.yahooapis.jp/ShoppingWebService/V1/categoryRanking'
    categoryUrl = 'http://shopping.yahooapis.jp/ShoppingWebService/V1/categorySearch'

    # init
    def __init__(self, appid):
        self.appid = appid  # appid : Your's application ID (required)

    # make request URL
    '''
    input : params(dict), output : url(string)
    "params" conforms to request parameters of Yahoo Shipping API
    '''
    def requestUrl(self, params):
        self.url = self.xmlUrl + '?appid=' + self.appid
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
        print self.url

    # get XML data from Yahoo
    def getXML(self):
        try:
            self.download = urllib2.urlopen(self.url, timeout=5)
            self.ret = self.download.read()
        except urllib2.HTTPError as e:
            print 'The server couldn\'t fulfill the request.'
            print 'Error code: ', e.code
        except urllib2.URLError as e:
            print 'We failed to reach a server.'
            print 'Reason: ', e.reason
        self.xml = BeautifulSoup(self.ret, 'xml')

    def saveXML(self, filepath):
        xmlFile = open(filepath, 'wb')
        xmlFile.write(self.ret)
        xmlFile.close()

    def insertSQL(self, sqlpath):
        #print self.xml.RankingData
        for RankingData in self.xml.find('Result').findAll('RankingData'):
            print RankingData.find('Code').string


class Rakuten:
    def __init__(self):
        pass


class Amazon:
    def __init__(self):
        pass