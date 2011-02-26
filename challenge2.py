"""
    Hyperpublic Challenge 2
    http://hyperpublic.com/challenge/question2

    Ivan Tam, ivan@hipnik.net.
"""

tiers = [ 98, 42, 23, 17, 3, 2 ]
staff = {
  "Doug":     {"points": 2349, "tasks": 0},
  "Jordan":   {"points": 2102, "tasks": 0},
  "Eric":     {"points": 2001, "tasks": 0},
  "Jonathan": {"points": 1747, "tasks": 0}
}

for s,v in staff.items():
  pts = v['points']
  print "=" * 10, s, pts
  for tier in tiers:
    tasks = 0
    tasks, pts = divmod( pts, tier )
    v['tasks'] += tasks
    print "%s for task %s tier, %s pts remain" % (tasks, tier, pts)
  print v['tasks'], " total"

print reduce( lambda x,y: x*y, [ v['tasks'] for k,v in staff.items() ])
