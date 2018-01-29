# Blueliv test [![Build Status](https://travis-ci.org/pedbermar/blueliv_test.svg?branch=master)](https://travis-ci.org/pedbermar/blueliv_test)
This project is a test on how to build a database-persistent python's subreddit crawler that exposes an API in order to show some statistics for the information we have gathered before.

# Assumptions, disign decisions
- Ubuntu 16.4, python 2.7, virtualenv
- A Mongodb database running on localhost at default port
- The information is read, stored and serve y JSON serialization format
- Falcon is the framework used to serve the REST API, becouse it is smaller,
  faster and more REST oriented than others frameworks
  
# Dependencies
- argparse, to parse args from the command line crawler usege 
- requests, to request reddit 
- json, for information serialization
- pymongo, the database adapter
- falcon, REST api framework

# Install
Clone the repo, move inside and
```sh
virtualenv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

# Test
```sh
pytest tests
```

# Usage
```sh
./blueliv_test.py 
usage: crawler.py [-h] -n NUMPAGES
crawler.py: error: argument -n/--numpages is required
```
Call it with -n option and a number of pages to crawl
```sh
python blueliv_test/crawler.py -n 3
```

# API usage
To run the API:
```sh
pip install gunicorn
gunicorn -b localhost:8001 blueliv_test.api
```

# API end points
## hello json
http://localhost:8001/

## Top 10 posts by score
http://localhost:8001/top10scores

## Top 10 posts by num of comments
http://localhost:8001/top10comm

## Top 5 authors by numbers of posts 
http://localhost:8001/top5authors

## Update databasde  
http://localhost:8001/update/2 num_of_page_to_crawl

## All posts of an author
http://localhost:8001/posts/pedbermar some_author
