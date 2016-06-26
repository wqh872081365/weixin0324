#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.template import RequestContext, Template
from django.views.decorators.csrf import csrf_exempt
from django.utils.encoding import smart_str, smart_unicode

import xml.etree.ElementTree as ET
import urllib, urllib2, time, hashlib
import datetime

from weixin0324.views_trans import replyCon
from weixin0324.views_weather import replyWea

TOKEN = "wangqihui0324"
TRANS = "0"
CHAT = "0"
WEATHER = "0"


@csrf_exempt
def handleRequest(request):
    if request.method == 'GET':
        # response = HttpResponse(request.GET['echostr'],content_type="text/plain")
        response = HttpResponse(checkSignature(request), content_type="text/plain")
        return response
    elif request.method == 'POST':
        # c = RequestContext(request,{'result':responseMsg(request)})
        # t = Template('{{result}}')
        # response = HttpResponse(t.render(c),content_type="application/xml")
        # response = HttpResponse(responseMsg(request), content_type="application/xml")
        # response = HttpResponse("")
        return parseTxtMsg(request)
    else:
        return None


def checkSignature(request):
    global TOKEN
    signature = request.GET.get("signature", None)
    timestamp = request.GET.get("timestamp", None)
    nonce = request.GET.get("nonce", None)
    echoStr = request.GET.get("echostr", None)

    token = TOKEN
    tmpList = [token, timestamp, nonce]
    tmpList.sort()
    tmpstr = "%s%s%s" % tuple(tmpList)
    tmpstr = hashlib.sha1(tmpstr).hexdigest()
    if tmpstr == signature:
        return echoStr
    else:
        return None


def parseTxtMsg(request):

    global TRANS
    global CHAT
    global WEATHER

    msg = ""

    xmlstr = smart_str(request.body)
    xml = ET.fromstring(xmlstr)
    ToUserName = smart_str(xml.find('ToUserName').text)
    FromUserName = smart_str(xml.find('FromUserName').text)
    CreateTime = smart_str(xml.find('CreateTime').text)
    MsgType = smart_str(xml.find('MsgType').text)
    Content = smart_str(xml.find('Content').text)
    MsgId = smart_str(xml.find('MsgId').text)

    if TRANS == "1" and CHAT == "0" and WEATHER == "0":
        if Content == 'exit1':
            msg = '感谢使用翻译模式，\r\n更多功能正在完善中！'
            TRANS = "0"
        else:
            msg = replyCon(Content)

    elif CHAT == "1" and TRANS == "0" and WEATHER == "0":
        if Content == 'exit2':
            msg = '感谢使用聊天模式，\r\n更多功能正在完善中！'
            CHAT = "0"
        else:
            msg = '聊天模式正在开发中。。。'

    elif WEATHER == "1" and TRANS == "0" and CHAT == "0":
        if Content == 'exit3':
            msg = '感谢使用天气查询模式，\r\n更多功能正在完善中！'
            WEATHER = "0"
        else:
            msg = replyWea(Content)

    elif CHAT == "0" and TRANS == "0" and WEATHER == "0":
        if Content == '1':
            msg = '请输入需要翻译的单词：'
            TRANS = "1"

        elif Content == '2':
            msg = '进入聊天模式：'
            CHAT = "1"

        elif Content == '3':
            msg = '请输入需要查询的城市：'
            WEATHER = "1"

        else:
            msg = '欢迎访问动漫分享平台，\r\n本公众号正在建设中，\r\n目前提供的服务有限，\r\n输入1进入翻译模式，\r\n输入2进入聊天模式，\r\n输入3进入天气查询模式，\r\n输入exit1退出翻译模式，\r\n输入exit2退出聊天模式，\r\n输入exit3退出天气查询模式，\r\n任意输入将重新收到本消息。'

    return sendTxtMsg(FromUserName, ToUserName, msg)


def sendTxtMsg(FromUserName,ToUserName,Content):
    reply_xml = """<xml>
    <ToUserName><![CDATA[%s]]></ToUserName>
    <FromUserName><![CDATA[%s]]></FromUserName>
    <CreateTime>%s</CreateTime>
    <MsgType><![CDATA[text]]></MsgType>
    <Content><![CDATA[%s]]></Content>
    </xml>""" % (FromUserName, ToUserName, datetime.datetime.now(), Content)

    return HttpResponse(reply_xml)

