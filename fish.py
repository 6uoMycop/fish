import itertools
import tarfile
import requests
import random
# import time
import whois
from nltk.corpus import wordnet


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


def is_available(url_in: str):
    try:
        whois.whois(url=url_in)
    except:
        return True
    return False


def analyze_word(word: str):
    n = 0  # number of ambiguous letters
    for c in word:
        if c in symbols.keys():
            n += 1
    return n / len(word)  # relative number of ambiguous letters


# generate phishing-safe domain name by keyword
# returns [list of lists of domain names], [list of evaluated numbers (less=better)], [list of listd of availability]
def generate_domain_name(keywords: list, toplevel: str = '.com', delim: str = '-'):
    domain_names = []
    synonyms = []
    synonyms_values = []  # evaluation values for corresponding words in synonyms list
    for kw in keywords:
        # generate synonyms
        synonims_i = [kw]
        for syn in wordnet.synsets(kw):
            for l in syn.lemmas():
                if l.name().isalpha():
                    synonims_i.append(l.name().lower())
        synonyms.append(list(set(synonims_i)))

        # eval
        values_i = []
        for w in synonims_i:
            values_i.append(analyze_word(w))
        synonyms_values.append(values_i)

    combinations = list(itertools.product(*synonyms))
    combinations_values = []
    permutations = []

    for elem in combinations:
        permutations.append(list(itertools.permutations(list(elem))))

        val = 0
        for i in range(len(elem)):
            val += synonyms_values[i][synonyms[i].index(elem[i])]
        combinations_values.append(val)

    for block in permutations:
        domain_names_i = []
        for elem in block:
            name = ''
            for word in elem:
                name += word
                name += delim
            name = name[:-len(delim)] if delim else name
            name += toplevel
            domain_names_i.append((name, is_available(name)))
        domain_names.append(domain_names_i)

    # pass  # TODO return ALL, sorted, with eval numbers
    return [x for _, x in sorted(zip(combinations_values, domain_names))], sorted(combinations_values)


# check_owner('google.com')
# random.seed(time.process_time())
# print(generate('google.com', 100))

names, values = generate_domain_name(['signal', 'quest'])
for i in range(len(names)):
    print("{:.2f}".format(values[i]) + " | " + str(names[i]))

