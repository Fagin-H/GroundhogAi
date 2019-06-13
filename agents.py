import numpy as np

class schedule:
    
    def __init__(self, sch):
        self.sch = sch
        
    def __str__(self):
        return str(self.sch)
    
    def __repr__(self):
        return str(self.sch)
    
    def curact(self, time): #returns current action wanting to be done given current time
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
        self.rs = {'self' : [1]} #relationships [like]
        self.inven = [] #inventory
        self.locations = {} #Known locations of people and items
        self.home = np.array([0,0]) #home location
        self.sch = schedule({}) #schedule
        self.stats = {'str' : 10,
                      'con' : 10,
                      'dex' : 10,
                      'int' : 10,
                      'wis' : 10,
                      'chr' : 10
                      }
        self.status = {'hun' : 1, #food
                       'thu' : 1, #water
                       'hp' : 5, #hp
                       'eng' : 1, #energy
                       'abl' : 0, #alcohol
                       'loc' : np.array([0,0]) #location
                       }
        self.desires = {}
        
    
    def __str__(self):
        return self.name

    def __repr__(self):
        return "Agent: {}".format(self.name)
    
    def look(self, world, dist = 10):
        for item in world['items']:
            if np.linalg.norm(world['items'][item].loc - self.status['loc']) < dist: #finds dist between item and self, if less than maximum dist then item added to known locations
                self.locations[item] = world['items'][item].loc
        
        for agent in world['agents']:
            if np.linalg.norm(world['agents'][agent].status['loc'] - self.status['loc']) < dist: #finds dist between agent and self, if less than maximum dist then agent added to known locations
                self.locations[agent] = world['agents'][agent].status['loc']
        
    
    def find_act(self):
        pass
    
    def action(self):
        pass





































