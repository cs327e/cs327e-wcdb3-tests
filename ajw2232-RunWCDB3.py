# RunWCDB3.py
# TechKnuckle Support



"""
To run the program
  % python RunWCDB3.py < RunWCDB3.in.xml > RunWCDB3.out.xml

To document the program
  % pydoc -w WCDB3
"""

# -------
# imports
# -------

import sys

from WCDB3 import WCDB_solve

# ----
# main
# ----

WCDB_solve(sys.stdin, sys.stdout)
