import sys, os
path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, path + '/../')

from blueliv_test.crawler import Crawler
import pytest

results = []
# Num of pages 
n = 5
r = Crawler()

def test_all_ok():
    assert r.version == 'v0.1'

# Go to reddit python subrredit and get the firsrt n pages
def test_get_n_pages():
    r = Crawler()
    results = r.get_subreddit(n)

    # Will fail if we dont get any results (Reddit Too Much Requests)
    assert results

    for r in results:
        assert results[0]['subreddit'] == "Python"
    
    # It will fail if the subreddit has len than n pages
    assert len(results) > 100*n

# For every submission gather: Submission title, external url, discussion url,
# submitter,punctuation, creation date and number of comments
def test_feed_parser():
    r = Crawler()
    feed = r.get_subreddit(2)
    assert feed
    results = r.feed_parser(feed)
    assert results
    for r in results:
        assert type(r.get('title')) == unicode
        assert type(r.get('eurl')) == unicode 
        assert type(r.get('durl')) == unicode
        assert type(r.get('author')) == unicode
        assert type(r.get('score')) == int
        assert type(r.get('created')) == float
        assert type(r.get('num_comm')) == int
        
# Persist the results in a database
def test_database():
    data = {
        "num_comm": 1, 
        "author": "pedbermar", 
        "created": 1515615418.0, 
        "url": "https://github.com/pedbermar/blueliv_test", 
        "title": "Pedro Berrocal githubprofile", 
        "link": "https://github.com/pedbermar/", 
        "punctuation": 1024
    }
    
    r = Crawler()
    assert r.update_db(data)
        
