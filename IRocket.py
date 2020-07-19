from p5 import *

class IRocket:
    Acceleration = 0.1
    size = Vector(2,30)
    vel = 0
    maxVel = 15
    angle = radians(20)
    miss = False
    hit = False

    def __init__(self,x,y):
        self.pos = Vector(x,y)
        
    def status(self):
        if not(-20 < self.pos.x < width+20) or not(-20 < self.pos.y < height+20) : 
            IRocket.miss = True
    
    def set_hit():
        IRocket.hit = True

    def move(self):
        if IRocket.miss or IRocket.hit:
            self.pos = Vector(-15,10)
        else:
            self.pos.x += IRocket.vel*sin(IRocket.angle)        
            self.pos.y -= IRocket.vel*cos(IRocket.angle)

    def show(self):
        with push_matrix():
            translate(self.pos.x, self.pos.y)
            rotate(IRocket.angle)
            fill(51,192,239)
            no_stroke()
            rect((-IRocket.size.x/2,-IRocket.size.y/2),IRocket.size.x,IRocket.size.y)
            stroke(0)
        
    def accelerate(self):
        if IRocket.vel < IRocket.maxVel :
            IRocket.vel += IRocket.Acceleration
    
    def rotateRight(self):
        if IRocket.vel > 1 :
            IRocket.angle += radians(10)
        
    def rotateLeft(self):
        if IRocket.vel > 1 :
            IRocket.angle -= radians(10)
                
