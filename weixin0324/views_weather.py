#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 天气查询功能（聚合数据-天气预报API）

import urllib, urllib2, time, hashlib

import json
from urllib import urlencode

appkey = "a974af8894474e9cbb45bc8130206d0f"


def paraseWeatherjson(res):
    replyContent = ''

    replyContent = "%s%s%s\n" % (replyContent, res['today']['city'].encode('utf-8'), '天气预报')
    replyContent = "%s%s\n" % (replyContent, res['today']['date_y'].encode('utf-8'))
    replyContent = "%s%s%s\n" % (replyContent,  '天气: ', res['today']['weather'].encode('utf-8'))
    replyContent = "%s%s%s\n" % (replyContent, '温度: ', res['today']['temperature'].encode('utf-8'))
    replyContent = "%s%s%s\n" % (replyContent, '湿度: ', res['sk']['humidity'].encode('utf-8'))
    replyContent = "%s%s%s" % (replyContent, '风速: ', res['today']['wind'].encode('utf-8'))
    # print replyContent
    return replyContent


def replyWea(Content):
    # 只得到天气预报的内容
    global appkey

    queryStr = Content
    m = "GET"


    url = "http://v.juhe.cn/weather/index"
    params = {
        "cityname": Content,  # 要查询的城市，如：温州、上海、北京
        "key": appkey,  # 应用APPKEY(应用详细页查询)
        "dtype": "json",  # 返回数据的格式,xml或json，默认json
        "format": "1"  # 未来6天预报(future)两种返回格式，1或2，默认1
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
            # print res["result"]
        else:
            replyWeather = 'error code'
            # print "%s:%s" % (res["error_code"], res["reason"])
    else:
        replyWeather = 'api error'
        # print "request api error"


    # req = urllib2.Request(url=youdaoURL)
    # result = urllib2.urlopen(req).read()

    # replyContent = paraseYouDaoXml(ET.fromstring(result))

    return replyWeather


def main():
    replyWea("上海")


if __name__ == '__main__':
    main()
