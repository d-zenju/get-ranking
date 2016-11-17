# -*- coding: utf-8 -*-

import Ranking

def main():
    yahoo = Ranking.Yahoo('dj0zaiZpPXFMYmpXVVh3N2NmUyZzPWNvbnN1bWVyc2VjcmV0Jng9Nzg-')
    params = {
        'category_id':'2494',
        'period':'daily'}
    yahoo.requestUrl(params)
    yahoo.getXML()
    print yahoo.url

if __name__ == '__main__':
    main()
