import sys
import re


# sys.argv[1] is *.md
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
    if (strs:=re.match(r'\s*(#+)(.*)',line)):
        if (htl:=len((ht:=strs.groups()[0]))) > 6:
            continue
        # space to - and squeeze unsupported chars
        rest = re.sub(r'\s','-', strs.groups()[1].strip())
        rest = re.sub(r'[^-_0-9a-zA-Z]', '', rest)
        print(''.join((' '*(htl-1)*4, '* ',
                       '[',strs.groups()[1].strip(),'](#', rest,')')))

