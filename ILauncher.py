from p5 import *
from IRocket import IRocket
from PLauncher import PLauncher
from NeuralNet import NeuralNet

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import math

class ILauncher:
    def __init__(self):
        self.pos = Vector(width/2, height)
        self.iRocket = IRocket(self.pos.x+6,self.pos.y-22)
        self.pLauncher = PLauncher()
        self.distance = [0.]*self.pLauncher.PRocketNum
        #self.brain = NeuralNet(2*self.pLauncher.PRocketNum,6,3,1)
        self.brain_tf = keras.Sequential([  layers.Dense(2, activation="relu", name="layer1"),
                                            layers.Dense(3, activation="relu", name="layer2"),
                                            layers.Dense(4, name="layer3"),
                                        ])
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
            self.pLauncher = PLauncher()
            self.distance = [0.]*self.pLauncher.PRocketNum
            self.testD = 0.

    
    def move(self):
        if self.dead :
            return 
        
        self.pLauncher.move()
        self.iRocket.move()
        #self.lifetime += 1 

        
    def show(self):
        if self.dead :
            return 
            
        self.iRocket.show()
        self.pLauncher.show()

    
    def radarDetections(self):
        if self.dead :
            a = [0.]*2*self.pLauncher.PRocketNum
            return a
        
        for i in range(self.pLauncher.PRocketNum):
            point1 = (self.iRocket.pos.x,self.iRocket.pos.y,0)
            point2 = (self.pLauncher.pRockets[i].pos.x,self.pLauncher.pRockets[i].pos.y,0)
            self.distance[i] = dist(point1,point2)
        
        a0 = 15/self.distance[0]
        d0 = (self.iRocket.pos).copy()
        #d0.sub(self.pLauncher.pRockets[0].pos)
        d0 = d0 - self.pLauncher.pRockets[0].pos
        k0 = (HALF_PI+atan2(d0.y,d0.x)-self.iRocket.angle)/(TWO_PI)
        
        #a1 = 15/self.distance[1]
        #d1 = (self.iRocket.pos).copy()
        #d1.sub(self.pLauncher.pRockets[1].pos)
        #k1 = (HALF_PI+atan2(d1.y,d1.x)-self.iRocket.angle)/(TWO_PI)
        
        if a0 > self.testD :
            self.testD = a0
                
        return [a0,k0]#,a1,k1]
    
            
    def interception(self,input):
        decision = self.brain_tf(tf.convert_to_tensor([input], dtype=tf.float32))
        maxIndex = tf.math.argmax(decision,1).numpy()[0]
        
        #decision = self.brain.output(input)   
        #max = decision[0]
        #maxIndex = 0
        #for i in range(len(decision)):
        #    if decision[i] > max :
        #        max = decision[i]
        #        maxIndex = i
                
        if maxIndex == 0 :
            self.iRocket.accelerate()
        if maxIndex == 1 :
            self.iRocket.rotateLeft()
        if maxIndex == 2 :
            self.iRocket.rotateRight()
            
            
    def clone(self):
        clone = ILauncher()
        #clone.brain = self.brain.clone()
        inputList = [0.]*2*self.pLauncher.PRocketNum
        clone.brain_tf(tf.convert_to_tensor([inputList]))
        clone.brain_tf.set_weights(self.brain_tf.get_weights()) 
        return clone
    
    def crossover(self,parent):
        child = ILauncher()
        #child.brain = self.brain.crossover(parent.brain)
        inputList = [0.]*2*self.pLauncher.PRocketNum
        child.brain_tf(tf.convert_to_tensor([inputList]))
        child.brain_tf.set_weights(self.brain_tf.get_weights())
        return child

    def mutate(self):
        list_of_weights = self.brain_tf.get_weights()
        noise = [np.random.normal(scale=0.2,size=arr.shape) for arr in list_of_weights]
        self.brain_tf.set_weights(np.add(self.brain_tf.get_weights(),noise))
        
        list_of_new_weights = []
        for element in self.brain_tf.get_weights():
            element[element>1] = 1
            element[element<-1] = -1
            list_of_new_weights.append(element)
        
        self.brain_tf.set_weights(list_of_new_weights)

        #self.brain.mutate(self.mutationRate)
        
    def calcFitness(self):
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
        
        
        
        
        
        
        
        
        
        
        
        
        
