import sys

class inception():
    level = 0
    level_max = 0
    current_level = 0
    def __init__(self,level_max=6):
        self.level_max=level_max
        
    def spinning_top(self):
        n = 1
        while True:
            if (n-1 > self.current_level) :
                print 'we can go deeper'
                print n-1
            try:
                sys._getframe(n)
            except ValueError:
                self.current_level = n - 1
                return n - 1
            
            n += 1
    
    def going_deeper(self):
        self.level = self.spinning_top()
        if self.level < self.level_max :
            self.level = self.spinning_top()
            y = self
            y.going_deeper().next()
            yield (self.level)
        yield(self.level)
        
            
        
        

Voyage = inception(5)
Voyage.spinning_top()
Voyage.going_deeper().next()
