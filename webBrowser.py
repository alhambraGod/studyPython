# -*- coding: utf-8 -*-
###########################################
import argparse
import mechanicalsoup
from getpass import getpass

###########################################
########### FAIL: mechanicalsoup ##########
def test_web_browser1():
    # parser = argparse.ArgumentParser(description='Login to GitHub.')
    # parser.add_argument('username')
    # args = parser.parse_args()
    # args.password = getpass('Please enter your GitHub password: ')

    username = 'ecaijw@msn.com'
    browser = mechanicalsoup.StatefulBrowser()
    browser.open("https://github.com")
    browser.follow_link("login")


    browser =mechanicalsoup.Browser()
    # uncomment for a more verbose output
    # browser.set_verbose(2)
    result = browser.get('https://github.com')
    # result = browser.get('http://baidu.com')
    print(result.soup.follow)
    # login = result.soup.select('#form')[0]
    # login.select("#kw")[0]['value'] = "ecaijw@msn.com"

##################################################
# RoboBrowser
##################################################
from robobrowser import RoboBrowser
def test_web_browser():
    browser = RoboBrowser(history=True)

    # start CGI server
    # python -m http.server --cgi 8080