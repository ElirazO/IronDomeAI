from p5 import *

class IRocket:
    Acceleration = 0.1
    size = Vector(2,30)
    maxVel = 15

    def __init__(self,x,y):
        self.pos = Vector(x,y)
        self.vel = 0
        self.angle = radians(20)
        self.miss = False
        self.hit = False

    def status(self):
        if not(-20 < self.pos.x < width+20) or not(-20 < self.pos.y < height+20) : 
            self.miss = True
    
    def set_hit():
        self.hit = True

    def move(self):
        if self.miss or self.hit:
            self.pos = Vector(-15,10)
        else:
            self.pos.x += self.vel*sin(self.angle)        
            self.pos.y -= self.vel*cos(self.angle)

    def show(self):
        with push_matrix():
            translate(self.pos.x, self.pos.y)
            rotate(self.angle)
            fill(51,192,239)
            no_stroke()
            rect((-IRocket.size.x/2,-IRocket.size.y/2),IRocket.size.x,IRocket.size.y)
            stroke(0)
        
    def accelerate(self):
        if self.vel < IRocket.maxVel :
            self.vel += IRocket.Acceleration
    
    def rotateRight(self):
        if self.vel > 1 :
            self.angle += radians(10)
        
    def rotateLeft(self):
        if self.vel > 1 :
            self.angle -= radians(10)
                
