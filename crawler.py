import os

try:
    import argparse
except ImportError:
    print("Trying to Install required module: argparse\n")
    os.system('pip3 install argparse')

import argparse

import pjcsv
import pjparser
import pjscraping
import pjgoogle

# -- argument parsing
ap = argparse.ArgumentParser()

ap.add_argument("-i", "--in", required=False, help="path to sites input csv file")
ap.add_argument("-s", "--search", required=False, help="path to search input csv file")

ap.add_argument("-o", "--out", required=True, help="path to output fetched urls csv file")

ap.add_argument("-p", "--proxies", required=False, help="path to input proxies csv file")

ap.add_argument("-m", "--matching", required=False, help="path to url matching csv file")
ap.add_argument("-r", "--result", required=False, help="path to output matched urls csv file")

args = vars(ap.parse_args())

sites = []

if args["in"]:
    # -- get site list from csv file
    sites = pjcsv.csv_in(args["in"])
elif args["search"]:
    # -- get site list from google
    searchs = pjcsv.csv_in(args["search"])
    for search in searchs:
        sites += pjgoogle.googlesearch(search)
else:
    print("-i/--in or -s/--search missing")
    exit(1)

# -- get proxies if set
proxies = []
if args["proxies"]:
    proxies = pjcsv.csv_in(args["proxies"])

# -- get src lists, www.aaa-bbb.com/ccc.php,www.aaa-bbb.com/,ccc.php
crawls = []
for site in sites:
    if len(proxies):
        crawl = pjparser.fetch_src(site, pjscraping.scrape_page_with_proxies(site, proxies))
        crawls += crawl
    else:
        crawl = pjparser.fetch_src(site, pjscraping.scrape_page(site))
        crawls += crawl

# -- output results
pjcsv.csv_out(args["out"], crawls)

#-- get matching if set
matching = []
if args["matching"]:
    matching = pjcsv.csv_in(args["matching"])

if len(matching):
    if args["result"]:
        matched_crawls = []
        for crawl in crawls:
            # -- check if url contatins any one of matching array
            if any(s in crawl[1] for s in matching):
                matched_crawls.append(crawl)
        
        # -- output matched result
        pjcsv.csv_out(args["result"], matched_crawls) 
    else:
        print("-r/--result missing path to output matched urls")