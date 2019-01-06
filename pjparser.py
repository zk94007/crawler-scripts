import os

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("Trying to Install required module: BeautifulSoup\n")
    os.system('pip3 install beautifulsoup4')

from bs4 import BeautifulSoup

# -- fetch src data
def fetch_src(url, text):
    html = BeautifulSoup(text, "html.parser")
    result = []
    for script in html.findAll('script'):
        src = script.get('src')
        if src:
            result.append([url] + parse(src))
    return result

# -- url parser
def parse(src):
    parsed = [src] + src.rsplit('/', 1)
    parsed[1] += "/"
    return parsed