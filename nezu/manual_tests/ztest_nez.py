from ..nezu import dbg

x = 13
dbg('x')
input = 12


def yolo():
    def yoyo():
        pass

    dbg('x')
    dbg('xx', 'x')
    dbg('globals')
    dbg('yolo', hide=3, note='hidden')
    dbg('yoyo')
    dbg('xx')
    dbg('input')


yolo()


class Dog:
    @staticmethod
    def sit(self):
        """wolololo"""
        pass

    def bark(self):
        dbg('self.sits')
        dbg('self.sit')
        # print(locals())


fifi = Dog()

fifi.bark()

# dbg({'x':x})
