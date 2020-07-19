from p5 import *

class PRocket:
    size = Vector(3,25)
    Gravity = 0.03
    miss = False
    hit  = False
    angle = radians(-random_uniform(40,10))
    vel = random_uniform(4,6)
    Xvel =  vel*sin(angle)
    Yvel = -vel*cos(angle)

    def __init__(self,x,y):
        self.pos  = Vector(x,y)
               
    def status(self):
        if -20 > self.pos.x or -20 > self.pos.y :
            PRocket.miss = True
        
        if self.pos.y > height + 20:
            PRocket.hit = True
                
    def move(self):
        if PRocket.miss or PRocket.hit:
            self.pos = Vector(-100,-100)       
        else:
            self.pos.x += PRocket.Xvel
            self.pos.y += PRocket.Yvel
            PRocket.Yvel += PRocket.Gravity
            PRocket.angle = atan(-PRocket.Xvel/PRocket.Yvel)
        
    def show(self):
        if PRocket.miss or PRocket.hit :
            pass
        else: 
            with push_matrix():
                translate(self.pos.x, self.pos.y)
                rotate(PRocket.angle)
                fill(0,230,0)
                no_stroke()
                rect((-PRocket.size.x/2,-PRocket.size.y/2),PRocket.size.x,PRocket.size.y)
                stroke(0)
            
    
   
