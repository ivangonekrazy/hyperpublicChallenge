"""
    Hyperpublic Challenge2
    http://hyperpublic.com/challenge/question1

    Ivan Tam, ivan@hipnik.net.
"""

import pprint
pp = pprint.PrettyPrinter(indent=2)

lines = []
f = None
try:
    f = open("challenge2input.txt")
    lines = f.readlines()
except IOError, e:
    print "Fail: %s" % str(e)
finally:
    if f: f.close()

influences = {}

users = {}
for i in xrange( len(lines) ):
    users[i] =[] 

for i,line in enumerate(lines):
    for j,user in enumerate(line):
        if user == 'X':
            users[i].append(j)

pp.pprint(users)
