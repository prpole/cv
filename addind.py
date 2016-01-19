#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Adds hanging indent LaTeX tag, as defined in cv.tex
"""

from pandocfilters import toJSONFilter, RawInline

def latex(s):
  return RawInline('latex', s)

def addind(k, v, f, meta):
  if k == 'Para':
     v.insert(0, latex('\\ind '))

if __name__ == "__main__":
  toJSONFilter(addind)
