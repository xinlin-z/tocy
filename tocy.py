import sys
import re


# python3 tocy.py[0] *.md[1]
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
    strs = re.search(r'^\s*(#+)(.*)', line)
    if strs:
        ht = strs.groups()[0]
        rest = strs.groups()[1].strip()
        htl = len(ht)
        print(''.join((' '*(htl-1)*4,
                       '* ',
                       '[',rest,']',
                       '(#','-'.join(rest.split()),')')))

