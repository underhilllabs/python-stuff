#!/usr/bin/env python
"""script to parse a .emx file from Emusic.com and download the mp3s"""

import sys
from BeautifulSoup import BeautifulSoup
import urllib2
import string 
import time
import os
import re

# change this to be your music directory
homedir = os.path.expanduser('~')
music_dir = homedir+"/Music/"

def urlify(s):
     # Replace all runs of whitespace with a single dash
     s = re.sub(r"\s+", '-', s)

     # Remove all non-word characters (everything except numbers and letters)
     s = re.sub(r"\W", '-', s)
     #print "s is ",s
     return s

def download_mp3s(soup_str):
    for murl in soup_str.findAll("trackurl"):
        lname = murl.string.split('/')[-1]
        lname = music_dir + mdir + lname
        print "Downloading: ",murl.string," -  Writing file out to: ",lname,"\n"
        u = urllib2.urlopen(murl.string)
        localFile = open(lname, 'w')
        localFile.write(u.read())
        localFile.close()
        #time.sleep(30)
    return True
        
if len(sys.argv) != 2:
    print "usage: ", sys.argv[0], "filename.emx\n"
    sys.exit(1)

fname = sys.argv[1]
f = open(fname)
fstr = f.read()
f.close()
soup = BeautifulSoup(fstr)
# create a directory for mp3s if it doesn't exist
martist = urlify(soup.findAll("artist")[0].string)
malbum = urlify(soup.findAll("album")[0].string)
mdir = martist + "/" + malbum + "/"
print "stripped mdir is " + music_dir + mdir, "\n"
if not os.path.exists(music_dir + mdir):
    os.makedirs(music_dir + mdir)

download_mp3s(soup)
    


