class PRocket:
    Gravity = 0.03
    def __init__(self,x,y):
        self.size = PVector(3,25)
        self.pos  = PVector(x,y)
        self.angle = radians(-random(10,40))
        self.vel = random(4,6)
        self.Xvel = self.vel*sin(self.angle)
        self.Yvel = -self.vel*cos(self.angle)
        self.miss  = False
        self.hit   = False
        
        
    def status(self):
        #if self.pos.x < -50 or self.pos.y < -20 or self.pos.y > height+20:
        if not(-20 < self.pos.x) or not(-20 < self.pos.y) :
            self.miss = True
        
        ## hit the city
        #if (self.pos.y > height) and (-50 < self.pos.x) and (self.pos.x < 220):
        if self.pos.y > height + 20:
            self.hit = True

                
    def move(self):
        if self.miss or self.hit:
            self.pos = PVector(-1000,-1000)       
        else:
            self.pos.x += self.Xvel
            self.pos.y += self.Yvel
            self.Yvel  += PRocket.Gravity
            self.angle  = atan(-self.Xvel/self.Yvel)
        
    def show(self):
        if self.miss or self.hit :
            pass
        else:
            pushMatrix()
            translate(self.pos.x,self.pos.y)
            rotate(self.angle)
            c = color(0,0,100)
            fill(0,230,0)
            noStroke()
            rect(-(self.size.x/2),-(self.size.y/2),self.size.x,self.size.y)
            stroke(0)
            popMatrix()
    
    
