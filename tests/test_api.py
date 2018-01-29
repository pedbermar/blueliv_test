import sys, os
path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, path + '/../')

import falcon
from falcon import testing
import pytest
import json
from blueliv_test.api import api
import pymongo

# Expose a REST API
@pytest.fixture
def client():
    return testing.TestClient(api)

def test_api(client):
    response = client.simulate_get('/')
    assert response.status == falcon.HTTP_OK

# Top 10 submissions by points
def test_top10score():
    response = client().simulate_get('/top10score')
    results = json.loads(response.content)
    # assert len(results) == 10
    prev_score = results[0]['score']
    for r in results[1:-1]:
        assert r['score'] <= prev_score
    assert response.status == falcon.HTTP_OK

# Top 10 discussed submissions
def test_top10comm():
    response = client().simulate_get('/top10comm')
    results = json.loads(response.content)
    # assert len(results) == 10
    prev_numcomm = results[0]['num_comm']
    for r in results[1:-1]:
        assert r['num_comm'] <= prev_numcomm
    assert response.status == falcon.HTTP_OK

# Create a way to update the information of the current archived
def test_updatedb():
    test = {
        'title': 'How to build a rest api in python',
        'durl': 'http://reddit.com/python/howotbuildapi',
        'eurl': 'http://example.com',
        'author': 'Pedro Berrocal',
        'num_comm': 0,
        'created': 10101010.00,
        'score': 0,
        'is_self': 'false'
    }

    testmod = {
        'title': 'How to build a rest api in python',
        'durl': 'http://reddit.com/python/howotbuildapi',
        'eurl': 'http://example.com',
        'author': 'pedbermar',
        'num_comm': 0,
        'created': 10101010.00,
        'score': 0,
        'is_self': 'false'
    }

    c = pymongo.MongoClient()
    db = c.blueliv_test
    db.reddit.insert(test)
    db.reddit.update({"durl": test['durl']}, testmod)
    result = db.reddit.find_one({"durl": test['durl']})
    assert result['author'] == 'pedbermar'

    response = client().simulate_get('/update/3')
    results = json.dumps(response.content)

    assert results
    assert response.status == falcon.HTTP_OK

    
# Create a way to retrieve top submitters
def test_top_authors():
    response = client().simulate_get('/posts/aphoenix')
    results = json.dumps(response.content)
    assert results
    assert response.status == falcon.HTTP_OK

# Add a way to query all posts by a user
# Add a way to query all posts a user commented
# Use of a Continuous Integration system (Hint: TravisCI)

