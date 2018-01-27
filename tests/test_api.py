import sys, os
path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, path + '/../')

import falcon
from falcon import testing
import pytest
import json
from blueliv_test.api import api

# Expose a REST API
@pytest.fixture
def client():
    return testing.TestClient(api)

def test_api(client):
    response = client.simulate_get('/')
    # result_doc = response.content
    # assert json.dumps(result_doc) == 'Blueliv python subreddit API'
    assert response.status == falcon.HTTP_OK

# Top 10 submissions by points
# Top 10 discussed submissions
# Create a way to update the information of the current archived
# Create a way to retrieve top submitters
# Add a way to query all posts by a user
# Add a way to query all posts a user commented
# Use of a Continuous Integration system (Hint: TravisCI)

