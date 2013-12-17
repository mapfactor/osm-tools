"""
  Script for parsing error logs into compact HTML page.
  usage:
     ./log2html <logfile1> [<logfile2>|...] > output.html
"""
import os
import sys

def extractRoundabouts( lines ):
  "return list of problematic way IDs (uniq, sorted)"
  ways = []
  roundaboutSection = False
  for line in lines:
    if 'fix_roundabout.py' in line:
      if "STARTED" in line:
        roundaboutSection = True
      elif "FINISHED" in line:
        roundaboutSection = False
      else:
        assert False, line # unexpected word combination
    if roundaboutSection and "WARNING" in line:
      ways.append( int( line.split()[-1] ) )
  return sorted(list(set(ways)))

def reportWays( title, wayIds ):
  ret = "<h3>" + title + "</h3>\n"
  for w in wayIds:
    ret += '<a href="http://www.openstreetmap.org/way/%d">http://www.openstreetmap.org/way/%d</a><br>\n' % ( w, w )
  return ret

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print __doc__
    sys.exit(-1)

  print """<html><head>
   <title>MapFactor OSM Data Processing - roundabouts report 2013.12</title>
</head><body>
<h1>MapFactor OSM Data Processing - roundabouts report 2013.12</h1>
"""
  for filename in sys.argv[1:]:
    ways = extractRoundabouts( open(filename) )
    if ways:
      print reportWays( os.path.basename(filename), ways )
  print "</body>"

