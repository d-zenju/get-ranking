# -*- coding: utf-8 -*-

import Init
import Ranking
import datetime
import time

def main():
    # config file path (templatefile : config.xml)
    confpass = 'pconfig.xml'

    # read config (yahooKey, rakutenKey, amazonKey, category)
    config = Init.Config(confpass)
    config.read()
    config.readCategory()

    # init get ranking methods
    yahoo = Ranking.Yahoo(config.yahooKey)
    #rakuten = Ranking.Rakuten(config.rakutenKey)
    #amazon = Ranking.Amazon(config.amazonKey)

    # make timestamp
    now = datetime.datetime.now()
    timestamp = now.strftime('%Y-%m-%d_%H-00-00')

    # branch category (site)
    for row in config.category:
        if row[0] == 'yahoo':       # if yahoo
            params = {
                'category_id':row[1],
                'period':'daily'
            }
            yahoo.requestUrl(params)
            yahoo.getXML()
            filename = './xml/yahoo/' + row[2]+ '_' + str(timestamp) + '.xml'
            yahoo.saveXML(filename)
            yahoo.insertSQL('./sql/test.sql')

        elif row[0] == 'rakuten':   # if rakuten
            pass
        elif row[0] == 'amazon':    # if amazon
            pass
        else:                       # no such category (site)
            print 'ERROR:: There is no such category (site): ' + row[0]

        time.sleep(1.0)

if __name__ == '__main__':
    main()
