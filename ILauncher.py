from p5 import *
from IRocket import IRocket
from PLauncher import PLauncher
from NeuralNet import NeuralNet

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import math
import inspect
import numpy as np

class ILauncher:
    next_id = 0
    def __init__(self):
        self.id = ILauncher.next_id
        ILauncher.next_id += 1
        self.pos = Vector(width/2, height)
        self.iRocket = IRocket(self.pos.x+6,self.pos.y-22)
        self.pLauncher = PLauncher()
        self.distance = [0.]*self.pLauncher.PRocketNum
        #self.brain = NeuralNet(2*self.pLauncher.PRocketNum,6,3,1)
        self.brain_tf = keras.Sequential([  layers.Dense(2, activation="relu", name="layer1"),
                                            layers.Dense(6, activation="relu", name="layer2"),
                                            layers.Dense(3, name="layer3"),
                                        ])
        self.dead = False
        self.lifetime = 0.
        self.score = 0
        self.fitness = 0.
        self.mutationRate = 0.05
        self.testD = 0.
        print("Generates ILauncher, ID: "+str(self.id))

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

        if self.dead:
            print("ILauncher, ID: "+str(self.id)+", is dead. Score: "+str(self.score))

    
    def move(self):
        if self.dead :
            return 
        
        self.pLauncher.move()
        self.iRocket.move()
        #self.lifetime += 1 

        
    def display(self):
        if self.dead :
            return 
            
        self.iRocket.display()
        self.pLauncher.display()

    
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
        inputList = [0.]*2*self.pLauncher.PRocketNum
        clone.brain_tf(tf.convert_to_tensor([inputList]))
        clone.brain_tf.set_weights(self.brain_tf.get_weights())
        #clone.brain_tf.set_weights(self.preTrain_weights())
        return clone
    
    def crossover(self,partner):
        child = ILauncher()
        inputList = [0.]*2*self.pLauncher.PRocketNum
        child.brain_tf(tf.convert_to_tensor([inputList]))
        
        self_weights = self.brain_tf.get_weights()
        partner_weights = partner.brain_tf.get_weights()

        for i,layer in enumerate(self_weights):
            for j in range(len(layer)):
                rand = np.random.random()
                if rand > 0.5 :
                    self_weights[i][j] = partner_weights[i][j]
        
        child.brain_tf.set_weights(self_weights)
            
        return child

    def mutate(self,randScale): #scale=0.075
        list_of_weights = self.brain_tf.get_weights()
        noise = [np.random.normal(scale=randScale,size=arr.shape) for arr in list_of_weights]
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
        self.fitness = self.score*self.score

    ## option 2
        #self.fitness = 1
        #self.fitness *= (1+self.score)
        #self.fitness *= pow(2,self.score)

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

    def preTrain_weights(self):
        preTrain_old = [np.array([[ 0.7747052 , -0.06323507],[ 0.650144  , -0.4070573 ]], dtype=float), 
                 np.array([-0.00159831,  0.02615436], dtype=float), 
                 np.array([[-0.08703193,  0.4317813 , -0.26286018, -0.19466951, -0.13379496, 0.15367594],
                     [-0.02992624, -0.19129099,  0.6304834 , -0.8421867 ,  0.24539606, -0.5280434 ]], dtype=float), 
                 np.array([ 0.01992389, -0.06196998, -0.11939131, -0.00367607,  0.00435869, -0.0057879 ], dtype=float), 
                 np.array([[ 0.42867652,  0.3649504 ,  0.3358565 ],
                     [-0.40823904, -0.37652016, -0.51416016],
                     [ 0.9031374 , -0.6544139 , -0.7731864 ],
                     [ 0.51811844,  0.32121518, -0.40145496],
                     [-0.13394707, -0.04317584, -0.35383993],
                     [ 0.41144678, -0.7426472 , -0.27136636]], dtype=float), 
                 np.array([-0.00285651, -0.07616875,  0.00990287], dtype=float)]
        
        preTrain = [np.array([[ 0.7732944 , -0.05998065],[ 0.7283419 , -0.38255513]], dtype=float), 
                    np.array([-0.04344827,  0.0136483 ], dtype=float), 
                    np.array([[-0.07711454,  0.50689536, -0.18772525, -0.14911102, -0.09128406, 0.14447917],
                            [-0.03839664, -0.17755915,  0.6494552 , -0.9088742 ,  0.18324763, -0.52563614]], dtype=float), 
                    np.array([-0.00230634, -0.06889542, -0.07750924, -0.06946152,  0.00666572, 0.02743732], dtype=float), 
                    np.array([[ 0.43108776,  0.3122723 ,  0.3690732 ],
                            [-0.37592992, -0.36520183, -0.4319192 ],
                            [ 0.97778624, -0.6643945 , -0.8000411 ],
                            [ 0.53290147,  0.32760376, -0.44241896],
                            [-0.15208031, -0.04004817, -0.29146948],
                            [ 0.4044475 , -0.7463187 , -0.2511852 ]], dtype=float), 
                    np.array([-0.05362742, -0.09179185, -0.01467659], dtype=float)]
        
        return preTrain
        
        
        
        
        
        
        
        
        
        
        
        
        
