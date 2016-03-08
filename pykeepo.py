#!/usr/bin/env python

import sys
import subprocess
import time

if (len(sys.argv) < 1):
  print "No stream given."

streamname = sys.argv[1]
prefix = "http://twitch.tv/"
url = prefix + streamname
suffix = "/chat?popout="

subprocess.Popen(["mpv", url])
time.sleep(1)
subprocess.Popen(["google-chrome", "--app=" + url + suffix])
