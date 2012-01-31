#!/usr/bin/python

# Author: Benjamin Waller <benjamin@mycontact.eu>
# based on pyanidb

import sys, os
import shlex, subprocess


if len(sys.argv) < 2:
	print "No folder supplied - is this being called from SABnzbd?"
	sys.exit()
else:
	command= "python " + os.path.join(os.path.dirname(sys.argv[0]), "anidb.py") + " -r -n -m -a -w -x '" + sys.argv[1] + "'"
	if (os.name != "posix"):
		args = shlex.split(command, posix=False)
	else
		args = shlex.split(command)
	retcode = subprocess.call(args)
	sys.exit(retcode)