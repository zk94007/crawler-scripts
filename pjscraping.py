import os

try:
    import requests
except ImportError:
    print("Trying to Install required module: requests\n")
    os.system('pip3 install requests')

try:
    from fake_useragent import UserAgent
except ImportError:
    print("Trying to Install required module: fake_useragent\n")
    os.system('pip3 install fake_useragent')

from urllib.parse import urlparse
from random import choice
from fake_useragent import UserAgent
from time import sleep

PROXIES = []
CURRENT_PROXY = ''

# -- set proxy
def set_proxy(session, proxy_candidates, verify=False):
    global CURRENT_PROXY
    """
    Configure the session to use one of the proxy_candidates.  If verify is
    True, then the proxy will have been verified to work.
    """
    while True:
        CURRENT_PROXY = choice(proxy_candidates)
        print("Trying with proxy: " + CURRENT_PROXY)
        session.proxies = {urlparse(CURRENT_PROXY).scheme: CURRENT_PROXY}
        if not verify:
            return
        try:
            print(session.get('https://httpbin.org/ip').json())
            return
        except Exception:
            pass

# -- scrape without proxy
def scrape_page(url):
    print('Starting srape page on url: ' + url)
    response = requests.get(url)
    return response.text
    # s = BeautifulSoup(plain, "html.parser")
    # return scrape_src(url, s)

# -- scrape with proxy
def scrape_page_with_proxies(url, proxy_candidates=PROXIES):
    print('Starting srape page on url: ' + url)
    ua = UserAgent()
    session = requests.Session()
    session.headers = {'User-Agent': ua.random}
    set_proxy(session, proxy_candidates=proxy_candidates)
    while True:
        try:
            response = session.get(url)
            break
        except Exception as e:
            session.headers = {'User-Agent': ua.random}
            set_proxy(session, proxy_candidates=proxy_candidates, verify=True)
            print("skipping...")
            sleep(0.3)
    print('Success with proxy: ' + CURRENT_PROXY)
    return response.text
    # s = BeautifulSoup(response.text, "html.parser")
    # return scrape_src(url, s)