import os
from p5 import *
from ILauncher import ILauncher
import time
import random

class Population:
    def __init__(self,size):
        self.size = size
        self.iLaunchers = [ILauncher() for i in range(self.size)]
        self.bestILauncher = None
        self.bestILauncherIndex = 0
        self.bestILauncherScore = 0
        self.bestFitness = 0.
        self.fitnessSum = 0.
        self.gen = 0
        self.showILauncher = 0
        self.time = 0

    def done(self,force_stop):
        if force_stop:
            return True

        for i in range(len(self.iLaunchers)):
            if not(self.iLaunchers[i].dead) :
                return False
        return True

    def updateLuncher(self, index):
        if not(self.iLaunchers[index].dead) :
            a = self.iLaunchers[index].radarDetections()
            self.iLaunchers[index].interception(a)
            self.iLaunchers[index].status()
            self.iLaunchers[index].move()
    
    def update(self):
        for i in range(len(self.iLaunchers)):
            self.updateLuncher(i)
           

    def display(self):
        self.iLaunchers[self.showILauncher].display()

        if self.time != second():
            self.time = second()
        else:
            return
        
        bestILauncherScore = 0
        for i in range(len(self.iLaunchers)):
            if self.iLaunchers[i].score > bestILauncherScore and self.iLaunchers[i].dead == False:
                bestILauncherScore = self.iLaunchers[i].score
                self.showILauncher = i
            
            
    def setBestILauncher(self):
        max = 0.
        maxIndex = 0
        for i in range(len(self.iLaunchers)):
            if self.iLaunchers[i].fitness > max :
                max = self.iLaunchers[i].fitness
                maxIndex = i
        
        if max > self.bestFitness :
            self.bestFitness = max
            self.bestILauncher = self.iLaunchers[maxIndex].clone()
            self.bestILauncherScore = self.iLaunchers[maxIndex].score
            self.bestILauncherIndex = maxIndex
        else:
            self.bestILauncher = self.bestILauncher.clone()
        
    def selectParant(self):
        parants_fitness = [-1,-1]
        parants_index = [0,0]
        for i in range(len(self.iLaunchers)):
            if self.iLaunchers[i].fitness > parants_fitness[0] :
                parants_fitness[1] = parants_fitness[0]
                parants_index[1] = parants_index[0]
                parants_fitness[0] = self.iLaunchers[i].fitness
                parants_index[0] = i
            elif self.iLaunchers[i].fitness > parants_fitness[1] : 
                parants_fitness[1] = self.iLaunchers[i].fitness
                parants_index[1] = i
        
        self.bestILauncherIndex = parants_index[0]
        self.bestILauncherScore = self.iLaunchers[parants_index[0]].score
        self.bestFitness = parants_fitness[0]
        print("selectParant: parants_index: "+str(parants_index)+", parants_fitness: "+str(parants_fitness))
        self.weights_logger(parants_index[0])
        
        return parants_index[0],parants_index[1]

        
    def naturalSelection(self):
        newILaunchers = []
      
        p_idx = self.selectParant()
        child = self.iLaunchers[p_idx[0]].crossover(self.iLaunchers[p_idx[1]])
        newILaunchers.append(child)

        for _ in range(1,len(self.iLaunchers)):
            brother = child.clone()
            scale = random.uniform(0,0.075)
            brother.mutate(scale)
            newILaunchers.append(brother)
                
        self.iLaunchers = newILaunchers
        self.gen += 1
        print("Generation: "+str(self.gen))
                        
    def mutate(self):
        for i in range(len(self.iLaunchers)):
            self.iLaunchers[i].mutate(i*0.0075)
            
    def calcFitness(self):
        for i in range(len(self.iLaunchers)):
            self.iLaunchers[i].calcFitness()
            
    def calcFitnessSum(self):
        self.fitnessSum = 0.
        for i in range(len(self.iLaunchers)):
            self.fitnessSum += self.iLaunchers[i].fitness


    def weights_logger(self,bestILuncherIdx):
        with open("weightd.log",'a') as fh:
            fh.write(str(self.iLaunchers[bestILuncherIdx].score))
            fh.write("\n")
            fh.write(str(self.iLaunchers[bestILuncherIdx].brain_tf.get_weights()))
            fh.write("\n")

