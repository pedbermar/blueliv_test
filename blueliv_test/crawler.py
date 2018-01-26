import argparse
import urllib2
import json
import time

class Crawler:
    def __init__(self):
        self.version = 'v0.1'
        self.subr = 'https://www.reddit.com/r/python.json?limit=100&count=100&after='

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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Blueliv python subreddit parser')
    parser.add_argument('-n', '--numpages', type=int, required=True, help='an integer for the accumulator')
    args = parser.parse_args()
    r = Crawler()
    results = r.get_subreddit(args.numpages)
    if results:
        for r in results:
            print json.dumps(r, indent=2)
