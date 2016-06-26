#! /usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Music(models.Model):
    name = models.CharField(max_length=100)  # 歌名
    singer = models.CharField(max_length=100)  # 歌手
    compose = models.CharField(max_length=100)  # 作曲
    album = models.CharField(max_length=200)  # 专辑
    time = models.CharField(max_length=100)  # 发行时间
    source = models.CharField(max_length=400)  # 出处
    label = models.CharField(max_length=500)  # 标签
    mark = models.CharField(max_length=100)  # 喜欢 收藏 下载
    length = models.CharField(max_length=100)  # 时长
    lyrics = models.TextField()  # 歌词
    url = models.CharField(max_length=200)  # 网易云链接
    description = models.TextField()  # 备注
    listener = models.TextField()  # 听者
    comment = models.TextField()  # 评论

