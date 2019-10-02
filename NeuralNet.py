from Matrix import Matrix

class NeuralNet:
    def __init__(self, input, hidden, output, hiddenLayers):
        self.iNodes = input;
        self.hNodes = hidden;
        self.oNodes = output;
        self.hLayers = hiddenLayers;
        
        self.weights = []
        self.weights.append(Matrix(self.hNodes,self.iNodes+1))
        
        for i in range(1,self.hLayers):
            self.weights.append(Matrix(self.hNodes,self.hNodes+1))
        
        self.weights.append(Matrix(self.oNodes,self.hNodes+1))
        
        for w in self.weights:
            w.randomize()
    
    def mutate(self,mr):
        for w in self.weights:
            w.mutate(mr)
    
    def output (self,inputsArr):
        #Input Layer
        inputs = Matrix.initializedVector(inputsArr)
        curr_bias = inputs.addBias()
        
        #Hidden Layer
        for i in range(self.hLayers):
            hidden_ip = self.weights[i].dot(curr_bias)
            hidden_op = hidden_ip.activate()
            curr_bias = hidden_op.addBias()
        
        #Output Layer
        output_ip = self.weights[-1].dot(curr_bias)
        output = output_ip.activate()
        
        return output.matrixToVector()
    
    def crossover(self,partner):
        child = NeuralNet(self.iNodes,self.hNodes,self.oNodes,self.hLayers)
        for i in range(len(self.weights)):
            child.weights[i] = self.weights[i].crossover(partner.weights[i])
        return child
        
    
    def clone (self):
        clone = NeuralNet(self.iNodes,self.hNodes,self.oNodes,self.hLayers)
        for i in range(0,len(self.weights)):
            clone.weights[i] = self.weights[i].clone()
        return clone
    
    def load(self,weight):
        for i in range(len(weights)):
            weights[i] = weight[i]
    
    @staticmethod
    def pull(self):
        model = self.weights.clone()
        return model
    
