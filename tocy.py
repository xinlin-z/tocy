import sys
import re


with open(sys.argv[1]) as f:
    lines = f.readlines()


skip = 0
for line in lines:
    # skip code block started with 4 space
    if line.startswith(' '*4):
        continue
    # skip ``` block
    if line.startswith('```'):
        skip = abs(skip-1)
    if skip: continue
    # search and print out #+ title
    if strs:=re.match(r'\s*(#+)(.*)',line):
        if (htl:=len((ht:=strs.groups()[0]))) > 6:  # max head level is 6
            continue
        rest = strs.groups()[1].strip()
        # git rid of markdown syntax elements ~*_
        while a:=re.search(r'([~*_]{1,2})(.*)\1',rest):
            rest = rest[:a.start()] + a.groups()[1] + rest[a.end():]
        rest = re.sub(r'\s', '-', rest)  # space --> -
        rest = re.sub(r'[^-_0-9a-zA-Z]', '', rest)  # squeeze other chars
        print(''.join((' '*(htl-1)*4, '* ',
                       '[',strs.groups()[1].strip(),'](#', rest,')')))

