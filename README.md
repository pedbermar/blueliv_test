# Blueliv test 
This project is a test on how to build a database-persistent python's subreddit crawler that exposes an API in order to show some statistics for the information we have gathered before.

# Assunmptions, disign decsions
- A Mongodb database running on localhost at default port
- A Reddit website request not returnig 'Too many requests'

# Dependencies
argparse, to parse args from the command line crawler use 
urllib2, to request reddit 
json, for information serialization
pymongo, the database adapter

# Install
Clone the repo, move inside and
```sh
virtualenv .venv
. .venv/bin/activate
pip install -r requeriments
```

# Test
```sh
pytest tests
```

# Usage
```sh
python blueliv_test/crawler.py 
usage: crawler.py [-h] -n NUMPAGES
crawler.py: error: argument -n/--numpages is required
```
Call it with -n option and a number of pages to crawl
```sh
python blueliv_test/crawler.py -n 3
```
