import sys
import re


# python3 tocy.py[0] *.md[1]
with open(sys.argv[1]) as f:
    lines = f.readlines()


for line in lines:
    line = line.strip()
    strs = re.match(r'(#+)(.*)', line)
    if strs:
        ht = strs.groups()[0]
        rest = strs.groups()[1].strip()
        htl = len(ht)
        print(''.join((' '*(htl-1)*4,
                       '* ',
                       '[',rest,']',
                       '(#','-'.join(rest.split()),')')))

