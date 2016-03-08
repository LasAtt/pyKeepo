#!/usr/bin/env python

import sys
import time
from subprocess import Popen, PIPE, STDOUT

try:
    from subprocess import DEVNULL # py3k
except ImportError:
    import os
    DEVNULL = open(os.devnull, 'wb')

if (len(sys.argv) < 1):
  print "No stream given."

streamname = sys.argv[1]
prefix = "http://twitch.tv/"
url = prefix + streamname
suffix = "/chat?popout="

Popen(["mpv", url], stdin=PIPE, stdout=DEVNULL, stderr=STDOUT)
Popen(["google-chrome", "--app=" + url + suffix], stdin=PIPE, stdout=DEVNULL, stderr=STDOUT)
sys.exit()
