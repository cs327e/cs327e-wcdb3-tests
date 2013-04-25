#!/usr/bin/env python

# ------------------------------
# cs327e-wcdb/WCDB3/RunWCDB3.py
# Team Virus
# Copyright (C) 2013
# ------------------------------

"""
To run the program
    % python RunWCDB3.py < RunWCDB3.in.xml > RunWCDB3.out.xml
    % chmod ugo+x RunWCDB3.py
    % RunWCDB3.py < RunWCDB3.in.xml > RunWCDB3.out.xml

To document the program
    % pydoc -w WCDB3
"""

# -------
# imports
# -------

import sys
from WCDB3 import *

# ----
# main
# ----

main(sys.stdin, sys.stdout)
