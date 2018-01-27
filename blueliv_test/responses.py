import json
import falcon
class Root(object):
    def on_get(self, req, resp):
        resp.body = json.dumps('Blueliv python subreddit API', indent=2)
        resp.status = falcon.HTTP_200
