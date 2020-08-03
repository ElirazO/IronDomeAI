from p5 import *

class PRocket:
    dim = Vector(3,25)
    Gravity = 0.03

    def __init__(self,x,y):
        self.pos  = Vector(x,y)
        self.vel = random_uniform(4,6)
        self.angle = radians(-random_uniform(40,10))
        self.Xvel =  self.vel*sin(self.angle)
        self.Yvel = -self.vel*cos(self.angle)
        self.hit  = False
        self.miss = False
               
    def status(self):
        if -20 > self.pos.x or -20 > self.pos.y :
            self.miss = True
        
        if self.pos.y > height + 20:
            self.hit = True
                
    def move(self):
        if self.miss or self.hit:
            self.pos = Vector(-100,-100)       
        else:
            self.pos.x += self.Xvel
            self.pos.y += self.Yvel
            self.Yvel += PRocket.Gravity
            self.angle = atan(-self.Xvel/self.Yvel)
        
    def display(self):
        if self.miss or self.hit :
            pass
        else: 
            with push_matrix():
                translate(self.pos.x, self.pos.y)
                rotate(self.angle)
                fill(0,230,0)
                no_stroke()
                rect((-PRocket.dim.x/2,-PRocket.dim.y/2),PRocket.dim.x,PRocket.dim.y)
                stroke(0)
            
    
   
