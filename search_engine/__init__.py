# -*- coding: utf-8 -*-
__author__ = 'masashi'

from flask import Flask
from pymongo import MongoClient
from urlparse import urlparse

app = Flask(__name__)
app.config.from_object('config')


MONGO_URL = app.config['MONGO_URL']
client = MongoClient(MONGO_URL)
db = client[urlparse(MONGO_URL).path[1:]]
collection = db["Index"]

from search_engine import views