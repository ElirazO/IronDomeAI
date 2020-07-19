from p5 import *

class Matrix:
    ## first constructor
    def __init__(self,r,c):
        self.rows = r
        self.cols = c
        self.matrix = [[0.] * self.cols for i in range(self.rows)]
    
    ## second constructor
    @classmethod
    def float(cls,m):
        rows = len(m)
        cols = len(m[0])
        return cls(rows,cols)
    
    @classmethod
    def initializedVector(cls,vector):
        vlen = len(vector)
        m = cls(vlen,1)
        for i in range(0,vlen):
            m.matrix[i][0] = vector[i]
        return m
    
    def dot(self,n):
        result = []
        result = Matrix(self.rows,n.cols)
        
        if self.cols == n.rows :
            for i in range(self.rows) :
                for j in range(n.cols):
                    sum = 0 
                    for k in range(self.cols):
                        sum += self.matrix[i][k]*n.matrix[k][j]
                    result.matrix[i][j] = sum
        return result
    
    def randomize(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] = random_uniform(-1,1)
    
    def matrixToVector(self):
        arr = []
        for i in range(self.rows):
            for j in range(self.cols):
                arr.append(self.matrix[i][j])
        return arr
    
    def addBias(self):
        n = Matrix(self.rows+1,1)
        for i in range(self.rows):
            n.matrix[i][0] = self.matrix[i][0]
        n.matrix[self.rows][0] = 1.
        return n
    
    def activate(self):
        n = Matrix(self.rows,self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                n.matrix[i][j] = self.relu(self.matrix[i][j])
        return n
    
    @staticmethod
    def relu(x):
        return max(0,x)
    
    def mutate(self,mutationRate):
        for i in range(self.rows) :
            for j in range(self.cols) :
                rand = random_uniform(1)
                if rand < mutationRate :
                    self.matrix[i][j] += random_gaussian()/5
                    
                    if self.matrix[i][j] > 1 :
                        self.matrix[i][j] = 1
                    if self.matrix[i][j] < -1 :
                        self.matrix[i][j] = -1
    
    def crossover(self,partner):
        child = Matrix(self.rows,self.cols)
        
        randR = floor(random_uniform(self.rows))
        randC = floor(random_uniform(self.cols))
        
        for i in range(self.rows):
            for j in range(self.cols):
                if i < randR or (i == randR and j <= randC) :
                    child.matrix[i][j] = self.matrix[i][j]
                else:
                    child.matrix[i][j] = partner.matrix[i][j];
        return child
    
    def clone(self):
        clone = Matrix(self.rows,self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                clone.matrix[i][j] = self.matrix[i][j]
        return clone
    

    



                    
                    
                    
                    
                    
                    
                    
                
        

    
