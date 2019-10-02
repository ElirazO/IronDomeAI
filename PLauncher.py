from PRocket import PRocket

class PLauncher:
    def __init__(self,width,height):
        self.size = PVector(50,50)
        self.randPosX = random(80,150) 
        self.pos = PVector(width-self.randPosX,height)
        self.PRocketNum = 1# int(random(1,3))
        self.pRockets = [PRocket(self.pos.x,self.pos.y) for i in range(self.PRocketNum)]
        self.refTime = millis()
        self.timeConst = 1500
        self.miss = False
        self.hit = False

        
    def status(self):
        for i in range(self.PRocketNum) :
            self.pRockets[i].status()
        
            if i == 0 :
                allMiss = self.pRockets[i].miss
            else :
                allMiss = allMiss and self.pRockets[i].miss
            
            if self.pRockets[i].hit : 
                self.hit = True
            
        if allMiss : 
            self.miss = True    
        
    def move(self):
        if self.miss :
            return
                    
        for i in range(self.PRocketNum) :
            time = millis()
            if time > (self.refTime+self.timeConst*i) :
                self.pRockets[i].move()
            
    def show(self):
        if self.miss :
            return
        
        for i in range(self.PRocketNum) :
            self.pRockets[i].show()
    
