# file.py
from nezu import nezu, say

nezu(1)

say('egg')			    # works on simple variables
say('ham.spam')		    # works on attributes
say('spam["spam"]')     # works on keys and indexes
say('print')		    # works on functions and build-ins
