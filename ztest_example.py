# file.py
from nezu import say, nezu

nezu(1)
spam = {'spam':'bacon'}
say('egg')			    # works on simple variables
say('ham.spam')		    # works on attributes
say('spam["spam"]')     # does NOT works on keys and indexes (yet?)
say('print')		    # works on functions and build-ins
