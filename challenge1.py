"""
    Hyperpublic Challenge2
    http://hyperpublic.com/challenge/question1

    Ivan Tam, ivan@hipnik.net.
"""

def readInput(filename="challenge1input.txt"):
  """ read the input file and return a list of
      readlines
  """
  lines = []
  f = None
  try:
      f = open(filename)
      lines = f.readlines()
  except IOError, e:
      print "IOError on opening: %s" % str(e)
  finally:
      if f: f.close()
  return lines

def inviteTable(lines):
  """ takes a list of the readlines and
      builds the table of who invited who
  """
  users = {}
  for i in xrange( len(lines) ):
      users[i] =[] 

  for i,line in enumerate(lines):
      for j,user in enumerate(line):
          if user == 'X':
              users[i].append(j)
  return users

def influence( user, debug=False ):
  """ given a user, return her influence
  """
  if users[user] == []:
    if debug: print "user %s has invited no one" % user
    return 0 
  else:
    i = len( users[user] ) 
    if debug: print "user %s has invited %s" % (user, ",".join([ str(x) for x in users[user]] ) )
    for u in users[user]:
      i += influence( u, debug )
  return i 

users = inviteTable( readInput() )

# yay, the top 3 influencers!
print sorted([ j for j,k in sorted([ (influence(x), x) for x in users.keys() ])[-3:] ])
