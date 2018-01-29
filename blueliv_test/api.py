import falcon
from .responses import Root, Top10Score, Top10Comm, Update, Top5Authors, AuthorPosts

api = application = falcon.API()
api.add_route('/', Root())
api.add_route('/top10score', Top10Score())
api.add_route('/top10comm', Top10Comm())
api.add_route('/update/{n:int}', Update())
api.add_route('/top5authors', Top5Authors())
api.add_route('/posts/{author}', AuthorPosts())

