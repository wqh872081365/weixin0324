#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 聊天功能（图灵机器人API）

import urllib, urllib2, time, hashlib

import json
from urllib import urlencode
import sys

apikey = "978c5ea229f8dbb3858d76b4413ae683"


def parasechatjson(res):
    replyContent = ''

    replyContent = "%s%s\n" % (replyContent, res.encode('utf-8'))
    # print replyContent
    return replyContent


def replyChat(Content):
    # 只得到下一条内容
    global apkey

    queryStr = Content
    m = "POST"


    url = "http://www.tuling123.com/openapi/api"
    params = {
        "key": apikey,  # 应用APIKEY(官网查询)
        "info": queryStr,  # 数据
        "userid": "wangqihui0324"  # 用户ID
    }
    params = urlencode(params)
    if m == "GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res["text"]:
        replychat = parasechatjson(res["text"])
        print replychat
    else:
        replychat = 'api error'
        # print "request api error"

    # req = urllib2.Request(url=youdaoURL)
    # result = urllib2.urlopen(req).read()

    # replyContent = paraseYouDaoXml(ET.fromstring(result))

    return replychat


def main():
    replyChat("你漂亮么")


if __name__ == '__main__':
    main()
