#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# code originally from Michael Klier 
#   -- licensed unded CC-NC-SA
#   http://www.splitbrain.org/blog/2010-12/12-from_scuttle_to_delicious
#
# 1. change username and password in urls below
# 2. change SCUTTLEDOMAIN to the domain of your scuttle site
 
# to export from a scuttle server to del.icio.us use these URLs
scuttle_url = 'http://username:password@SCUTTLEDOMAIN/api/posts_all.php'
delicious_url = 'https://username:password@api.del.icio.us/v1/posts/add'

# to export links from delicious into a scuttle site use these two URLs 
scuttle_add = 'http://username:password@SCUTTLEDOMAIN/scuttle/api/posts_add.php'
delicious_get = 'https://username:password@api.del.icio.us/v1/posts/all'

import sys 
import time
import urllib
from xml.dom import minidom
 
def main():
    delicious_raw = urllib.urlopen(delicious_get).read()
    delicious_xml = minidom.parseString(delicious_raw);
    bookmarks = delicious_xml.getElementsByTagName('post')
    count = bookmarks.length
 
    for bookmark in bookmarks:
        post = {}
        post['url'] = bookmark.getAttribute('href').encode('utf-8')
        post['description'] = bookmark.getAttribute('description').encode('utf-8')
        post['tags'] = bookmark.getAttribute('tag').encode('utf-8')
        post['dt'] = bookmark.getAttribute('time').encode('utf-8')
        post['shared'] = 'no'
        post['extended'] = bookmark.getAttribute('extended').encode('utf-8') 
        result = urllib.urlopen(scuttle_add, urllib.urlencode(post)).read()
        print count
        count = count - 1 
        time.sleep(1.5)
 
    return 0
 
if __name__ == '__main__':
    sys.exit(main())
