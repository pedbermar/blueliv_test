import argparse
import urllib2
import json
import time
import pymongo
import requests

class Crawler:
    def __init__(self):
        self.version = 'v0.1'
        self.subr = 'https://www.reddit.com/r/python.json?limit=100&count=100&after='
        self.headers = {
            'Host': 'www.reddit.com',
            'User-Agent': '/r/python example',
            'Accept': '*/*',
            'Accept-Language': 'en-US',
            'X-Requested-With': 'XMLHttpRequest',
            'Connection': 'keep-alive',
            'Save-Data': 'on',
        }
 
        client = pymongo.MongoClient()
        self.db = client.blueliv_test

    def get_subreddit(self, n):
        results = []
        nextpage = ''
        for i in range(n):
            try:
                # req = urllib2.Request(self.subr, None, self.headers)
                # file = urllib2.urlopen(req)
                data = requests.get(self.subr, headers=self.headers)
                # file = urllib2.urlopen(self.subr + nextpage)
            except:
                return False
	    # text = file.read()
	    # page = json.loads(text)['data']

            page = json.loads(data.text)
            # print page
	    nextpage = page['data']['after']
	    children = page['data']['children']
            for c in children:
                data = c['data']
                results.append(data)
            # time.sleep(10)
        if len(results) > 0:
            return results
        else:
            return False

    def feed_parser(self, feed):
        results = []
        for f in feed:
            result = {
                'title': f['title'],
                'durl': f['permalink'],
                'eurl': f['url'],
                'author': f['author'],
                'num_comm': int(f['num_comments']),
                'created': f['created_utc'],
                'score': int(f['score']),
                'is_self': f['is_self']
            }
            results.append(result)
        return results

    def update_db(self, r):
        try:
            result = self.db.reddit.find_one({"title": r['title']})
            if result == None:
                self.db.reddit.insert(r)
            else:
                self.db.reddit.update({"title": r['title']}, r)
            return True
        except:
            return False

    def update(self, n):
        results = self.get_subreddit(n)
        dic = self.feed_parser(results)
        if dic:
            for result in dic:
                self.update_db(result)

            return True
        else:
            return False
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Blueliv python subreddit parser')
    parser.add_argument('-n', '--numpages', type=int, required=True, help='an integer for the accumulator')
    args = parser.parse_args()
    r = Crawler()
    r.update(args.numpages)
        #     print json.dumps(r, indent=2)
