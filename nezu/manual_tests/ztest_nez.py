from ..nezu import say

x = 13
say('x')
input = 12
def yolo():
    def yoyo():
        pass

    say('x')
    say('xx', 'x')
    say('globals')
    say('yolo', hide=3, note='hidden')
    say('yoyo')
    say('xx')
    say('input')

yolo()

class Dog:
    @staticmethod
    def sit(self):
        '''wolololo'''
        pass
    def bark(self):
        say('self.sits')
        say('self.sit')
        # print(locals())

fifi = Dog()

fifi.bark()

# say({'x':x})
