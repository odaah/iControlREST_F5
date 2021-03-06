#!/usr/bin/env python
"""
ppjson.py
Convert JSON data to human-readable form.
(Reads from stdin and writes to stdout)
"""
import sys
import simplejson as json
print json.dumps(json.loads(sys.stdin.read()), indent=4)
sys.exit(0)
