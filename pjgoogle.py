import os

try:
    from fake_useragent import UserAgent
except ImportError:
    print("Trying to Install required module: fake_useragent\n")
    os.system('pip3 install fake_useragent')

try:
    from googlesearch import search
except ImportError:
    print("Trying to Install required module: google\n")
    os.system('pip3 install google')

from googlesearch import search
from fake_useragent import UserAgent

def googlesearch(keyword):
    ua = UserAgent()
    sites = []
    for url in search(keyword, stop=50, user_agent=ua.random, safe="on"):
        sites.append(url)
    return sites[:10]