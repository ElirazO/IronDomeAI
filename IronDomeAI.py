from p5 import *
from ILauncher import ILauncher
from Population import Population

#global width, height
keyArray = [False]*4
humanPlaying = False
drawOnly = False
#frame_rate = 60 
#img0Mask = None
img0 = None
img1Mask = None
img2 = None
img3 = None
pop = None
Launcher = None
#f = None

def setup():
    global Launcher, pop, humanPlaying
    size(1024,576)
    #smooth()
    global img0 , img2, img3
    #no_tint()
    img0 = load_image("data/back.jpg")
    #img1Mask = load_image("data/gaza.png")
    #img0.mask(img1Mask)
    #imageMode("CENTER")

    #img2 = load_image("data/iron_dome.png")
    #img3 = load_image("data/tel_aviv.png")
    #Launcher = ILauncher()

    #f = create_font("Arial.tiff", 16)

    if not(humanPlaying):
        pop = Population(50)
    else:
        Launcher = ILauncher()
    
def draw():
    global humanPlaying, drawOnly, img0 #, img1
    background(img0)
    
    if not(humanPlaying) :     
        if pop.done() :
            pop.calcFitness()
            pop.naturalSelection()
        else:
            pop.update()
            pop.display()
        
        fill(255)
        text("AI IRON DOME",(450,45))
        text("BEST LAUNCHER : "+str(pop.bestILauncherIndex),(width-200,65))
        text("BEST SCORE : "+str(pop.bestILauncherScore),(width-200,85))
        text("BEST FITNESS : "+str(floor(pop.bestFitness)),(width-200,105))
        text("GEN : "+str(pop.gen),(width-200,125))
        text("SHOW LAUNCHER : "+str(pop.showILauncher),(50,65))
        text("SCORE : "+str(pop.iLaunchers[pop.showILauncher].score),(50,85))
    
    else:
        #text_font(f, 36)

        fill(255)
        text("IRON DOME GAME",(450,45))
        
        _ = Launcher.radarDetections()
        Launcher.status()
        Launcher.move()
        Launcher.show()
        
        #### Multi Key Pressing
        if keyArray[0] :
            Launcher.iRocket.accelerate()
        if keyArray[1] :
            Launcher.iRocket.rotateLeft()
        if keyArray[2] :
            Launcher.iRocket.rotateRight()
    
    ###################################################
    
    #image(img1,(width-220,height-100))
    #image(img2,(width/2-15,height-80))
    #image(img3,(0,height-100))
    #fill(100)
    #no_stroke()
    #rect(width-350,height-40,5,40)
    #stroke(0)
    
    #if keyArray[3]:
    #    save_frame("frames/pic_####.png")


def key_pressed(event):
    if event.key == "UP" :
        keyArray[0] = True
    if event.key == "LEFT" :
        keyArray[1] = True
    if event.key == "RIGHT" :
        keyArray[2] = True
    if event.key == "SHIFT" :
        keyArray[3] = True

def key_released(event):
    if event.key == "UP" :
        keyArray[0] = False
    if event.key == "LEFT" :
        keyArray[1] = False
    if event.key == "RIGHT" :
        keyArray[2] = False
    if event.key == "SHIFT" :
        keyArray[3] = False

if __name__ == '__main__':
    run(frame_rate = 60)
        
   
            

    
