#!/usr/bin/env python

import os
import sys

logfile = sys.argv[1]
domain_keyword = sys.argv[2]

cmds = "cat $logfile | jq '[.[] | select(.domain==\"$domain_keyword\")]'  > result$domain_keyword.json && cat result$domain_keyword.json".replace("$logfile",logfile).replace("$domain_keyword",domain_keyword)

os.system(cmds)
