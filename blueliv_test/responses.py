import json
import falcon
import pymongo
from pymongo import MongoClient
from blueliv_test.crawler import Crawler

client = MongoClient()
db = client.blueliv_test

class Root(object):
    def on_get(self, req, resp):
        resp.body = json.dumps('Blueliv python subreddit API', indent=2)
        resp.status = falcon.HTTP_200

class Top10Score(object):
    def on_get(self, req, resp):
        top_score = [doc for doc in db.reddit.find({}, {"_id":0}).sort(
            [("score", pymongo.DESCENDING)]
        )][0:10]

        resp.body = json.dumps(top_score, indent=2)
        resp.status = falcon.HTTP_200

class Top10Comm(object):
    def on_get(self, req, resp):
        top_comm = [doc for doc in db.reddit.find({}, {"_id":0}).sort(
            [("num_comm", pymongo.DESCENDING)]
        )][0:10]
        resp.body = json.dumps(top_comm, indent=2)
        resp.status = falcon.HTTP_200

class Update(object):
    def on_get(self, req, resp, n):
        r = Crawler()
        resp.body = json.dumps(r.update(n), indent=2)
        resp.status = falcon.HTTP_200

class Top5Authors(object):
    def on_get(self, req, resp):
        top_authors = db.reddit.aggregate(
            [
                {"$group": {"_id": "$author", "count": {"$sum": 1}}}
            ]
        )['result'][0:5]
        resp.body = json.dumps(top_authors, indent=2)
        resp.status = falcon.HTTP_200

class AuthorPosts(object):
    def on_get(self, req, resp, author):
        aposts = [doc for doc in db.reddit.find({'author': author}, {"_id":0})]
        resp.body = json.dumps(aposts, indent=2)
        resp.status = falcon.HTTP_200
