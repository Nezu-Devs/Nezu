# file.py
from ..nezu import nezu, say
nezu(1)

egg = 3
ham = int()
spam = {'spam':'bacon'}

say('egg')          # works on simple variables
say('ham.real')     # works on attributes
say('print')        # works on functions and build-ins
say('spam["spam"]') # DOES NOT work on keys and indexes yet
