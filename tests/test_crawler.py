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
    results = r.get_subreddit(n)

    # Will fail if we dont get any results (Reddit Too Much Requests)
    assert results
    
    # It will fail if the subreddit has len than n pages
    assert len(results) > 100*n

# For every submission gather: Submission title, external url, discussion url,
# submitter,punctuation, creation date and number of comments

# Persist the results in a database
