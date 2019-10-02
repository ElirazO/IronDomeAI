class IRocket:
    Acceleration = 0.1
    def __init__(self,x,y):
        self.pos = PVector(x,y)
        self.size = PVector(2,30)
        self.vel = 0 #must be some initial velocity in detection
        self.maxVel = 15
        self.angle = radians(20)
        self.miss = False
        self.hit = False
        
    def status(self):
        if not(-20 < self.pos.x < width+20) or not(-20 < self.pos.y < height+20) : 
                self.miss = True
        
        # IRocket out of control after 10 sec
    
    def move(self):
        if self.miss or self.hit:
            self.pos = PVector(-15,10)
        else:
            self.pos.x += self.vel*sin(self.angle)        
            self.pos.y -= self.vel*cos(self.angle)

    def show(self):
        pushMatrix()
        translate(self.pos.x,self.pos.y)
        rotate(self.angle)
        fill(51,192,239)
        noStroke()
        rect(-(self.size.x/2),-(self.size.y/2),self.size.x,self.size.y)
        stroke(0)
        popMatrix()
        
    def accelerate(self):
        if self.vel < self.maxVel :
            self.vel += IRocket.Acceleration
    
    def rotateRight(self):
        if self.vel > 1 :
            self.angle += radians(10)
        
    def rotateLeft(self):
        if self.vel > 1 :
            self.angle -= radians(10)
                
