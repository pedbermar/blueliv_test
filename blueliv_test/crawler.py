import argparse
import urllib2
import json
import time
import pymongo

class Crawler:
    def __init__(self):
        self.version = 'v0.1'
        self.subr = 'https://www.reddit.com/r/python.json?limit=100&count=100&after='
        client = pymongo.MongoClient()
        self.db = client.blueliv_test

    def get_subreddit(self, n):
        results = []
        nextpage = ''
        for i in range(n):
            try:
                file = urllib2.urlopen(self.subr + nextpage)
            except:
                return False
	    text = file.read()
	    page = json.loads(text)['data']
	    nextpage = page['after']
	    children = page['children']
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
                'score': int(f['score'])
            }
            results.append(result)
        return results

    def update_db(self, r):
        try:
            result = self.db.reddit.find_one({"title": r['title']})
            if result == None:
                self.db.breddit.insert(r)
            else:
                self.db.reddit.update({"title": r['title']}, r)
            print 'Database updated'
            return True
        
        except:
            return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Blueliv python subreddit parser')
    parser.add_argument('-n', '--numpages', type=int, required=True, help='an integer for the accumulator')
    args = parser.parse_args()
    r = Crawler()
    results = r.get_subreddit(args.numpages)
    if results:
        for r in results:
            update_db(r)
        #     print json.dumps(r, indent=2)
