# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# xueqiu_data.py


import requests
import json
import time

import urllib3
urllib3.disable_warnings()

import io

import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

headers_xueqiu = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
                  # 'Cookie': 'aliyungf_tc=AQAAAIucjhjSrQwAaof5cmfIuM4VvIx+; s=e518qm2kjx; xq_a_token=3450822dc3b6c0b631c3ba4768fcddac23c054d7; xq_r_token=0de8d3b6155ce156310ff6d4e214d4532198ccec; Hm_lvt_1db88642e346389874251b5a1eded6e3=1555064605; u=431555064605338; device_id=58f4b654f91f32567fd610acaf81fcf5; __utmc=1; __utmz=1.1555064606.1.1.utmcsr=github.com|utmccn=(referral)|utmcmd=referral|utmcct=/tdzhang/pre_interview/blob/master/questions/%E7%88%AC%E8%99%AB%EF%BC%88%E9%AB%98%E7%BA%A7%EF%BC%89.md; __utma=1.837747656.1555064606.1555067915.1555071140.3; __utmt=1; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1555071254; __utmb=1.2.10.1555071140'
                  }

symbol_data, name_data, current_data, turnover_rate_data, market_capital_data, pe_ttm_data = [], [], [], [], [], []

for i in range(1, 5):

    millis = int(round(time.time() * 1000))
    # print(millis)

    xueqiu_res = requests.get(
        'https://xueqiu.com/service/v5/stock/screener/quote/list?page=' + str(i) + '&size=30&order=desc&orderby=percent&order_by=percent&market=US&type=us&_=' + 'millis', verify=False, headers=headers_xueqiu)
    # print(json.loads(xueqiu_res.text)['data'])

    # print(json.loads(xueqiu_res.text)['data']['list'])

    # print(len(json.loads(xueqiu_res.text)['data']['list']))
    print('\n')
    for i in json.loads(xueqiu_res.text)['data']['list']:
        symbol_data.append(i['symbol'])   # 股票代码
        name_data.append(i['name'])
        current_data.append(i['current'])
        turnover_rate_data.append(i['turnover_rate'])
        market_capital_data.append(i['market_capital'])
        pe_ttm_data.append(i['pe_ttm'])


import pandas as pd
aa = {'股票代码': symbol_data, '股票名称': name_data, '当前价': current_data,
      '涨跌幅': turnover_rate_data, '市值': market_capital_data, '市盈率': pe_ttm_data}

bb = pd.DataFrame(aa)
bb.to_csv("xueqiu.csv", encoding="utf-8")
