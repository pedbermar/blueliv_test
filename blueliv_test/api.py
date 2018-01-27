import falcon
from blueliv_test.crawler import Crawler
from .responses import Root

api = application = falcon.API()
api.add_route('/', Root())

