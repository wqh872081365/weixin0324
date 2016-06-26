# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.template import RequestContext, Template
from django.views.decorators.csrf import csrf_exempt
from django.utils.encoding import smart_str, smart_unicode

import xml.etree.ElementTree as ET
import urllib, urllib2, time, hashlib


@csrf_exempt
def handle_request(request):
    if request.method == 'GET':
        response = HttpResponse(check_signature(request),content_type="text/plain")
        return response
    elif request.method == 'POST':
        response = HttpResponse(response_msg(request),content_type="application/xml")
        return response
    else:
        return HttpResponse("Hello world ")


def check_signature(request):
    token = "wangqihui0324"
    signature = request.GET.get("signature")
    timestamp = request.GET.get("timestamp")
    nonce = request.GET.get("nonce")
    echostr = request.GET.get("echostr")
    signature_tmp = [token,timestamp,nonce]
    #lexicographical sorting
    signature_tmp.sort()
    #string concatenation
    # signature_tmp = ''.join(signature_tmp)
    signature_tmp = "%s%s%s" % tuple(signature_tmp)
    #sha1 encryption
    signature_tmp = hashlib.sha1(signature_tmp).hexdigest()
    #compare with signature
    if signature_tmp == signature:
        return echostr
    else:
        return HttpResponse("Hello world ! ")


def response_msg(request):
    #get post message
    msg = request.body
    #parser xml format
    msg_xml = ET.fromstring(msg)
    msg = {}
    for element in msg_xml:
        msg[element.tag] = smart_str(element.text)
    # content = msg.get('Content')
    # url_get_base = "http://api.ltp-cloud.com/analysis/?"
    # api_key = "YourApikey"
    # format = "plain"
    # pattern = "pos"
    #call for ltp-cloud api
    # result = urllib2.urlopen(url_get_base + 'api_key='+api_key+'&text='+content+'&format='+format+'&pattern='+pattern)
    # content = result.read().strip()
    content = "1"
    response = "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%d</CreateTime><MsgType><![CDATA[%s]]></MsgType><Content><![CDATA[%s]]></Content></xml>"
    #generate xml formt response
    response = response % (msg['FromUserName'],msg['ToUserName'],int(time.time()),'text',content)
    return response
