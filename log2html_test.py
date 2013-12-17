from log2html import *
import unittest

class Log2htmlTest( unittest.TestCase ):
  def testExtractRoundabouts( self ):
    self.assertEqual( extractRoundabouts( "Hello world" ), [] )
    self.assertEqual( extractRoundabouts( """2013-12-13 00:07:06,691 - INFO - STARTED['./fix_roundabout.py', 'localhost', 'osm_germany_2013_12_north_mff']
2013-12-13 00:07:07,429 - WARNING - cleaning flag for 246480890
2013-12-13 00:07:07,492 - WARNING - cleaning flag for 225658989
2013-12-13 00:07:07,518 - WARNING - cleaning flag for 225658991
2013-12-13 00:07:07,537 - WARNING - cleaning flag for 99705550
2013-12-13 00:07:08,238 - WARNING - cleaning flag for 227580983
2013-12-13 00:07:08,239 - WARNING - cleaning flag for 227578418
2013-12-13 00:07:09,231 - WARNING - cleaning flag for 28534690
2013-12-13 00:07:10,037 - WARNING - cleaning flag for 180099180
2013-12-13 00:07:10,755 - INFO - FINISHED['./fix_roundabout.py', 'localhost', 'osm_germany_2013_12_north_mff']
""".split("\n") ), [28534690, 99705550, 180099180, 225658989, 225658991, 227578418, 227580983, 246480890 ] )


  def testReportWays( self ):
    self.assertEqual( reportWays( "roundabout", [123,456] ), """<h3>roundabout</h3>
<a href="http://www.openstreetmap.org/way/123">http://www.openstreetmap.org/way/123</a><br>
<a href="http://www.openstreetmap.org/way/456">http://www.openstreetmap.org/way/456</a><br>
""" )


if __name__ == "__main__":
  unittest.main() 

