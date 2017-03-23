# -*- coding: utf-8 -*-
###########################################

from bs4 import BeautifulSoup
from bs4 import SoupStrainer
from html.parser import HTMLParser
from io import StringIO
# import urllib.parse
from urllib.parse import urljoin
from urllib.request import urlopen
from html5lib import parse, treebuilders

URLs = (
    # 'http://python.org',
    # 'http://google.com'
    # 'http://baidu.com',
    'http://google.cn',
)

def output(x):
    print('\n'.join(sorted(set(x))))

def simpleBS(url, f):
    'simpleBS() - use BeautifulSoup to parse all tags to get anchors'
    # output(urljoin(url, x['href']) for x in BeautifulSoup(f, 'lxml').findAll('a'))
    result = list(x for x in BeautifulSoup(f, 'lxml').findAll())
    print(result)
    # output(result)

def fasterBS(url, f):
    'fasterBS() - use BeautifulSoup to parse only anchor tags'
    output(urljoin(url, x['href']) for x in BeautifulSoup(f, parse_only=SoupStrainer('a')))

def htmlparser(url, f):
    'htmlparser() - use HTMLParser to parse only anchor tags'
    class AnchorParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            if not hasattr(self, 'data'):
                self.data = []
            if tag!= 'a':
                return
            for attr in attrs:
                if attr[0] == 'href':
                    self.data.append(attr[1])
    parser = AnchorParser()
    parser.feed(f.read())
    output(urljoin(url, x) for x in parser.data)

def html5libparser(url, f):
    'html5libparser() - use html5lib to parse anchor tags'
    output(urljoin(url, x.attributes['href'])
           for x in parse(f) if isinstance(x, treebuilders.simpletree.Element) and x.name == 'a')
    ########### simpletree not found ###################

def process(url, data):
    print('\n*** simple BS ***')
    simpleBS(url, data)
    data.seek(0)

    # print('\n*** faster BS ***')
    # fasterBS(url, data)
    # data.seek(0)
    #
    # print('\n*** HTML parser ***')
    # htmlparser(url, data)
    # data.seek(0)

    # print('\n*** HTML5lib ***')
    # html5libparser(url, data)

def main():
    # f = urlopen(url)
    # html = urlopen("http://www.google.cn").read()
    # print(html.decode())
    for url in URLs:

        f = urlopen(url)
        print("f.read(): ", f.read())
        data = StringIO(str(f.read()))
        f.close()
        process(url, data)


def parse_elsie():
    soup = BeautifulSoup(open('elsie.html'), 'lxml')
    # print(soup)
    # print(soup.prettify())

    result = list(x['href'] for x in soup.findAll('a'))
    print(result)

def parse_web():
    soup = BeautifulSoup(urlopen('http://google.cn'), 'lxml')
    soup = BeautifulSoup(urlopen('http://baidu.com'), 'lxml')
    soup = BeautifulSoup(urlopen('http://www.jb51.net/article/65287.htm'), 'lxml')

    # print(soup)
    # result = list(x['href'] for x in soup.findAll('a'))
    result = list()
    for x in soup.findAll('a'):
        if x.has_attr('href'):
            result.append(x['href'])
        else:
            result.append(str(x) + ' - HREF NOT FOUND')

    # result = list(x for x in soup.findAll('a'))
    print(result)

def parse_links_test():
    parse_elsie()
    parse_web()

if __name__ == '__main__':
    main()
