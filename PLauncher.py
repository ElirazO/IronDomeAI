from p5 import *
from PRocket import PRocket

class PLauncher:
    miss = False
    hit = False

    def __init__(self):
        self.size = Vector(50,50)
        self.randPosX = random_uniform(150,80) 
        self.pos = Vector(width - self.randPosX, height)
        self.PRocketNum = 1 # int(random(1,3))
        self.pRockets = [PRocket(self.pos.x,self.pos.y) for i in range(self.PRocketNum)]
        #self.refTime = millis()
        #self.timeConst = 1000
        
    def status(self):
        allMiss = True
        for i in range(self.PRocketNum) :
            self.pRockets[i].status()
            allMiss = allMiss and self.pRockets[i].miss

            if self.pRockets[i].hit : 
                PLauncher.hit = True
            
        if allMiss : 
            PLauncher.miss = True    
        
    def move(self):
        if PLauncher.miss :
            return
                    
        #for i in range(self.PRocketNum) :
        #    time = millis()
        #    if time > (self.refTime+self.timeConst*i) :
        #        self.pRockets[i].move()
        for i in range(self.PRocketNum) :
            self.pRockets[i].move()

            
    def show(self):
        if PLauncher.miss :
            return

        for i in range(self.PRocketNum) :
            self.pRockets[i].show()
    
    def get_PRocketNum(self):
        return self.PRocketNum
    
