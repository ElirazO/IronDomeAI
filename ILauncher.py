from IRocket import IRocket
from PLauncher import PLauncher
from NeuralNet import NeuralNet

class ILauncher:
    def __init__(self,width,height):
        self.pos = PVector(width/2,height)
        self.size = PVector(50,30)
        self.iRocket = IRocket(self.pos.x+6,self.pos.y-22)
        self.pLauncher = PLauncher(width,height)
        self.distance = [0.]*self.pLauncher.PRocketNum
        self.brain = NeuralNet(2*self.pLauncher.PRocketNum,6,3,1)
        self.dead = False
        self.lifetime = 0.
        self.score = 0
        self.fitness = 0.
        self.mutationRate = 0.05
        self.testD = 0.

        
    def status(self):
        for i in range(self.pLauncher.PRocketNum):
            if self.distance[i] < 20 :
                self.iRocket.hit = True
                self.pLauncher.pRockets[i].miss = True
                self.score += 1

        self.pLauncher.status()
        self.iRocket.status()
        
        #if self.iRocket.hit or self.iRocket.miss:
        if self.iRocket.hit :#or self.iRocket.miss:
            self.iRocket = IRocket(self.pos.x,self.pos.y)
        
        if self.pLauncher.hit :
            self.iRocket.miss = True
            self.dead = True 
        
        if self.pLauncher.miss : 
            self.pLauncher = PLauncher(width,height)
            self.distance = [0.]*self.pLauncher.PRocketNum
            self.testD = 0.

    
    def move(self):
        if self.dead :
            return 
        
        self.pLauncher.move()
        self.iRocket.move()
        self.lifetime += 1 

        
    def show(self):
        if self.dead :
            return 
        
        self.pLauncher.show()
        self.iRocket.show()

    
    def radarDetections(self):
        if self.dead :
            a = [0.]*2*self.pLauncher.PRocketNum
            return a
        
        for i in range(self.pLauncher.PRocketNum):
            self.distance[i] = dist(self.iRocket.pos.x,self.iRocket.pos.y,self.pLauncher.pRockets[i].pos.x,self.pLauncher.pRockets[i].pos.y)
        
        a0 = 15/self.distance[0]
        d0 = (self.iRocket.pos).copy()
        d0.sub(self.pLauncher.pRockets[0].pos)
        k0 = (HALF_PI+atan2(d0.y,d0.x)-self.iRocket.angle)/(TWO_PI)
        
        #a1 = 15/self.distance[1]
        #d1 = (self.iRocket.pos).copy()
        #d1.sub(self.pLauncher.pRockets[1].pos)
        #k1 = (HALF_PI+atan2(d1.y,d1.x)-self.iRocket.angle)/(TWO_PI)
        
        if a0 > self.testD :
            self.testD = a0
                
        return [a0,k0]#,a1,k1]
    
    def radarChooseTarget(self):
        print("HI")
            
    def interception(self,input):
        decision = self.brain.output(input)      
        max = 0
        maxIndex = 0
        for i in range(len(decision)):
            if decision[i] > max :
                max = decision[i]
                maxIndex = i
        
        if maxIndex == 0 :
            self.iRocket.accelerate()
        if maxIndex == 1 :
            self.iRocket.rotateLeft()
        if maxIndex == 2 :
            self.iRocket.rotateRight()
            
            
    def clone(self):
        clone = ILauncher(width,height)
        clone.brain = self.brain.clone()
        return clone
    
    def crossover(self,parent):
        child = ILauncher(width,height)
        child.brain = self.brain.crossover(parent.brain)
        return child

    def mutate(self):
        self.brain.mutate(self.mutationRate)
        
    def calcFitness(self):
    ## Don't forget how the natural selection works
    ## option 1
        #self.fitness = self.score*self.score

    ## option 2
        self.fitness = 1
        self.fitness *= (1+self.score)
        self.fitness *= pow(2,self.score)

    ## option 3
        #self.fitness = self.score * self.score
        #self.fitness *= 10*self.testD
        
    ##option 4
        # if self.score < 5 :
        #     self.fitness = 1+self.score
        #     self.fitness *= pow(2,2500/self.lifetime)
        #     #IRocketlifetime
        # else:
        #     self.fitness = 1
        #     self.fitness *= (1+self.score)
        #     self.fitness *= pow(2,self.score)
        
        
        
        
        
        
        
        
        
        
        
        
        
