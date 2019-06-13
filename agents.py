import numpy as np


class schedule:
    
    def __init__(self, sch):
        self.sch = sch
        
    def __str__(self):
        return str(self.sch)
    
    def __repr__(self):
        return str(self.sch)
    
    def curact(self, time):
        closest = 24
        for ts in self.sch:
            if float(ts) >= time and float(ts) < float(closest):
                closest = ts
        if closest != 24:
            return self.sch[closest]
        else:
            return None


class agent:
    
    def __init__(self, name):
        self.name = name
        self.rs = {'self' : 1}
        self.inven = []
        self.home = ""
        self.sch = schedule({})
        self.stats = {'str' : 10,
                      'con' : 10,
                      'dex' : 10,
                      'int' : 10,
                      'wis' : 10,
                      'chr' : 10
                      }
        self.status = {'hun' : 1,
                       'thu' : 1,
                       'hp' : 5,
                       'eng' : 1,
                       'abl' : 0,
                       }
        self.desires = {}
        
    
    def __str__(self):
        return self.name

    def __repr__(self):
        return "Agent: {}".format(self.name)
    
    