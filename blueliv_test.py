#!/usr/bin/env python
import sys, os
path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, path)

import argparse
from blueliv_test.crawler import Crawler

def main():
    parser = argparse.ArgumentParser(description='Blueliv python subreddit parser')
    parser.add_argument('-n', '--numpages', type=int, required=True, help='an integer for the accumulator')
    args = parser.parse_args()
    r = Crawler()
    r.update(args.numpages)
        #     print json.dumps(r, indent=2)



if __name__ == "__main__":
    main()
