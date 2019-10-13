#!/usr/bin/env python
# -*- coding: utf-8 -*-
from instgramApi import InstagramAPI
from random import randint
import time
import sys



USERNAME = "your instagram username here"
PASSWORD = "your instagram password here"

bot = InstagramAPI(USERNAME,PASSWORD)
bot.login()
bot.getUsernameInfo('cats')
print bot.LastJson
