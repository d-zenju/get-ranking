# -*- coding: utf-8 -*-

import Init
import Ranking

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

    # branch category (site)
    for row in config.category:
        if row[0] == 'yahoo':       # if yahoo
            params = {
                'category_id':row[1],
                'period':'daily'
            }
            yahoo.requestUrl(params)
            yahoo.getXML()
            print row[2]

        elif row[0] == 'rakuten':   # if rakuten
            pass
        elif row[0] == 'amazon':    # if amazon
            pass
        else:                       # no such category (site)
            print 'ERROR:: There is no such category (site): ' + row[0]
        
    """
    yahoo = Ranking.Yahoo(config.yahooKey)
    params = {
        'category_id':'2494',
        'period':'daily'}
    yahoo.requestUrl(params)
    yahoo.getXML()
    print yahoo.xml
    """

if __name__ == '__main__':
    main()
