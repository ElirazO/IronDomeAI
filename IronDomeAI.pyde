from ILauncher import ILauncher
from Population import Population

width = 1024
height = 576
keyArray = [False]*4

humanPlaying = False
drawOnly = False


if not(humanPlaying) :
    pop = Population(width,height,80)
else:
    Launcher = ILauncher(width,height)

def setup(): 
    size(width,height)
    frameRate(60)
    smooth()
    global img0, img1, img2, img3, rec
    img0 = loadImage("back.png")
    img1 = loadImage("gaza.png")
    img2 = loadImage("iron_dome.png")
    img3 = loadImage("tel_aviv.png")
    
def draw():
    global humanPlaying , mosque, drawOnly 
    image(img0,0,0)

            
    if not(humanPlaying) :     
        if pop.done() :
            pop.calcFitness()
            pop.naturalSelection()
        else:
            pop.update()
            pop.show()
        
        fill(255)
        text("AI IRON DOME",450,45)
        text("BEST LAUNCHER : "+str(pop.bestILauncherIndex),width-200,65)
        text("BEST SCORE : "+str(pop.bestILauncherScore),width-200,85)
        text("BEST FITNESS : "+str(floor(pop.bestFitness)),width-200,105)
        text("GEN : "+str(pop.gen),width-200,125)
        text("SHOW LAUNCHER : "+str(pop.showILauncher),50,65)
        text("SCORE : "+str(pop.iLaunchers[pop.showILauncher].score),50,85)
    
    else:
        fill(255)
        text("IRON DOME GAME",450,45)
        
        a = Launcher.radarDetections()
        Launcher.status()
        Launcher.move()
        Launcher.show()
        
        #### Multi Key Pressing
        if keyArray[0] :
        #if a[0] > 0.04 :
            Launcher.iRocket.accelerate()
        if keyArray[1] :
        #if a[1] < 0.5 :
            Launcher.iRocket.rotateLeft()
        if keyArray[2] :
        #if a[1] > 0.5 :
            Launcher.iRocket.rotateRight()
    
    ###################################################
    
    image(img1,width-220,height-100)
    image(img2,width/2-15,height-80)
    image(img3,0,height-100)
    fill(100)
    noStroke()
    rect(width-350,height-40,5,40)
    stroke(0)
    
    if keyArray[3]:
        saveFrame("frames/pic_####.png")


def keyPressed():
    if key == CODED :
        if keyCode == UP :
            keyArray[0] = True
        if keyCode == LEFT :
            keyArray[1] = True
        if keyCode == RIGHT :
            keyArray[2] = True
        if keyCode == SHIFT :
            keyArray[3] = True

    
def keyReleased():
    if key == CODED :
        if keyCode == UP :
            keyArray[0] = False
        if keyCode == LEFT :
            keyArray[1] = False
        if keyCode == RIGHT :
            keyArray[2] = False
        if keyCode == SHIFT :
            keyArray[3] = False



    
        
   
            

    
