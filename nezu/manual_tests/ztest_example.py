# file.py
from ..nezu import nezu, dbg

nezu(1)

egg = 3
ham = int()
spam = {'spam': 'bacon'}

dbg('egg')          # works on simple variables
dbg('ham.real')     # works on attributes
dbg('print')        # works on functions and build-ins
dbg('spam["spam"]')   # DOES NOT work on keys and indexes yet
