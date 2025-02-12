#!/usr/bin/env python3
import sysconfig
import site
import sys

DEST=sys.argv[1]

if DEST in sysconfig.get_paths()['purelib']:
    print(sysconfig.get_paths()['purelib'])
elif DEST in site.USER_SITE:
    print(site.USER_SITE)
else:
    exit(1)
