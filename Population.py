import os
from p5 import *
from ILauncher import ILauncher
from multiprocessing import Process, current_process

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
        self.time = millis()+7000

    def done(self):
        for i in range(len(self.iLaunchers)):
            if not(self.iLaunchers[i].dead) :
                return False
        return True

    def updateLuncher(self, index):
        if not(self.iLaunchers[index].dead) :
            #print("process ID: "+str(os.getpid()))
            a = self.iLaunchers[index].radarDetections()
            self.iLaunchers[index].interception(a)
            self.iLaunchers[index].status()
            self.iLaunchers[index].move()
    
    def update(self):
        #processes = []
        for i in range(len(self.iLaunchers)):
            self.updateLuncher(i)
            #process = Process(target=self.updateLuncher, args=(i,))
            #processes.append(process)
            #process.start()

    def show(self):
        self.iLaunchers[self.showILauncher].show()
        
        if self.time < millis() :
            self.time += 7000
        else:
            return
        
        bestILauncherScore = 0
        for i in range(len(self.iLaunchers)):
            if self.iLaunchers[i].score > bestILauncherScore :
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
        rand = random_uniform(self.fitnessSum)
        summation = 0
        for i in range(len(self.iLaunchers)):
            summation += self.iLaunchers[i].fitness
            if summation > rand : 
                return self.iLaunchers[i]
        
        return self.iLaunchers[0]
        
    def naturalSelection(self):
        newILaunchers = [ILauncher() for i in range(self.size)]
        self.setBestILauncher()
        self.calcFitnessSum()
        
        newILaunchers[0] = self.bestILauncher.clone()
        
        for i in range(1,len(self.iLaunchers)):
            child = self.selectParant().crossover(self.selectParant())
            child.mutate()
            newILaunchers[i] = child
        
        self.iLaunchers = newILaunchers
        self.gen += 1
                        
    def mutate(self):
        for i in range(len(self.iLaunchers)):
            self.iLaunchers[i].mutate()
            
    def calcFitness(self):
        for i in range(len(self.iLaunchers)):
            self.iLaunchers[i].calcFitness()
            
    def calcFitnessSum(self):
        self.fitnessSum = 0.
        for i in range(len(self.iLaunchers)):
            self.fitnessSum += self.iLaunchers[i].fitness
