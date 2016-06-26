#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 天气查询功能（聚合数据-天气预报API）

from django.http import HttpResponse
from django.template import RequestContext, Template
from django.views.decorators.csrf import csrf_exempt
from django.utils.encoding import smart_str, smart_unicode

import xml.etree.ElementTree as ET
import urllib, urllib2, time, hashlib

import json
from urllib import urlencode

appkey = "a974af8894474e9cbb45bc8130206d0f"


def paraseWeatherjson(res):
    replyContent = ''

    replyContent = "%s%s%s\n" % (replyContent, res['data']['realtime']['city_name'], '天气预报')
    replyContent = "%s%s\n" % (replyContent, res['data']['realtime']['date'])
    replyContent = "%s%s%s\n" % (replyContent,  '天气: ', res['data']['realtime']['weather']['info'])
    replyContent = "%s%s%s\n" % (replyContent, '温度: ', res['data']['realtime']['weather']['temperature'])
    replyContent = "%s%s%s\n" % (replyContent, '湿度: ', res['data']['realtime']['weather']['humidity'])
    replyContent = "%s%s%s%s\n" % (replyContent, '风速: ', res['data']['realtime']['wind']['direct'], res['data']['realtime']['wind']['power'])
    return replyContent


def replyWea(Content):
    # 只得到天气预报的内容
    global appkey

    queryStr = Content
    m = "GET"


    url = "http://op.juhe.cn/onebox/weather/query"
    params = {
        "cityname": Content,  # 要查询的城市，如：温州、上海、北京
        "key": appkey,  # 应用APPKEY(应用详细页查询)
        "dtype": "json",  # 返回数据的格式,xml或json，默认json
    }
    params = urlencode(params)
    if m == "GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            replyWeather = paraseWeatherjson(res["result"])
            print res["result"]
        else:
            print "%s:%s" % (res["error_code"], res["reason"])
    else:
        print "request api error"


    # req = urllib2.Request(url=youdaoURL)
    # result = urllib2.urlopen(req).read()

    # replyContent = paraseYouDaoXml(ET.fromstring(result))

    return replyWeather

