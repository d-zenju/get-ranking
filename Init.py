# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

# class : for read config file
class Config:
    def __init__(self, filepath):
        self.filepath = filepath

    def read(self):
        config = BeautifulSoup(open(self.filepath), 'lxml')
        self.yahooKey = config.yahoo.appid.contents[0]
        self.rakutenKey = config.rakuten.applicationid.contents[0]
        self.amazonKey = {
            'accesskey':config.amazon.awsaccesskeyid.contents[0],
            'secretaccesskey':config.amazon.secretaccesskey.contents[0],
            'associatetag':config.amazon.associatetag.contents[0]
            }
        self.category = config.category.filepath.contents[0];