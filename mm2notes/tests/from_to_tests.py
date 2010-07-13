#!/usr/bin/env python
#

"""One-line documentation for from_to_tests module.

A detailed description of from_to_tests.
"""

__author__ = 'scottakirkwood@gmail.com (Scott Kirkwood)'

import mm2notes.mm2notes as mm2notes
import unittest
import codecs
import glob
import difflib

class FromToTests(unittest.TestCase):
  def RunOne(self, mm_file, html_file):
    mm2n = mm2notes.Mm2Notes()
    lines = mm2n.open(mm_file)
    test_name = 'last_output.html'
    outfile = codecs.open(test_name, 'w', 'utf-8')
    mm2n.set_order_by_time(False)
    mm2n.write(outfile, lines)
    assert False == self.CompareFiles(html_file, test_name)

  def CompareFiles(self, good_file, test_file):
    diff = difflib.Differ()
    good_lines = open(good_file).read().splitlines()
    test_lines = open(test_file).read().splitlines()
    diffs = diff.compare(good_lines, test_lines)
    differs = False
    for line in diffs:
      if not line.startswith('  '):
        if not differs:
          differs = True
          print 'Files %s and %s differ' % (good_file, test_file)
        print line
    return differs

  def runTest(self):
    for fname in glob.glob('*.mm'):
      fnamehtml = fname.replace('.mm', '.html')
      self.RunOne(fname, fnamehtml)

    

if __name__ == '__main__':
  unittest.main() 
