# -*- coding: utf-8 -*-

import Init
import Ranking

def main():
    # config file pass (templatefile : config.xml)
    confpass = 'pconfig.xml'

    # read config (yahooKey, rakutenKey, amazonKey)
    config = Init.Config(confpass)
    config.read()

    yahoo = Ranking.Yahoo(config.yahooKey)
    params = {
        'category_id':'2494',
        'period':'daily'}
    yahoo.requestUrl(params)
    yahoo.getXML()
    print yahoo.xml

if __name__ == '__main__':
    main()
