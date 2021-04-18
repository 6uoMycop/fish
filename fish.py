import tarfile
import requests
import random
import time
import whois


def refresh_db():
    url = 'https://github.com/mitchellkrogza/Phishing.Database/raw/master/ALL-phishing-domains.tar.gz'
    fname = 'db.tar.gz'
    r = requests.get(url, allow_redirects=True)
    open(fname, 'wb').write(r.content)
    tar = tarfile.open(fname, "r:gz")
    tar.extractall()
    tar.close()


def search(url_in: str):
    url = url_in + '\n'
    with open('ALL-phishing-domains.txt', 'r') as F:
        for line in F:
            if url == line:
                return True
    return False


symbols = {
    'l': ('1'),
    '1': ('l'),
    'o': ('0', 'c', 'e'),
    '0': ('o'),
    'c': ('o', 'e'),
    'e': ('c'),
    'q': ('p', 'g'),
    'p': ('q', 'g'),
    'g': ('p', 'q'),
    'i': ('j'),
    'j': ('i'),
    'h': ('n'),
    'n': ('h'),
    'b': ('d'),
    'd': ('b'),
    's': ('5'),
    '5': ('s')
}


def generate(url_in: str, number=10):
    result = []
    for i in range(number):
        result.append('')
        for c in url_in:
            if c in symbols.keys():
                p = random.randint(0, len(symbols.get(c)))
                if not p:
                    result[i] += c
                else:
                    result[i] += symbols.get(c)[p-1]
            else:
                result[i] += c
    res_set = set(result)
    res_set.discard(url_in)
    return sorted(list(res_set))


def check_owner(url_in: str):
    try:
        w = whois.whois(url=url_in)
    except:
        print('Host down')
        return
    org = w['org']
    if org is None:
        print('Organisation\'s name unspecified. Unreliable domain')
    else:
        print('Organisation name: ' + org)
