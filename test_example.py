# file.py
from nezu import say

say('egg')			# works on simple variables
say('ham.spam')		# works on attributes
say('spam["spam"]') # works on keys and indexes
say('print')		# works on functions and build-ins