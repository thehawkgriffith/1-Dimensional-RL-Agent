import numpy as np
class Environment:
    
    def __init__(self):
        self.span = ['X', '-', '-', '-', '-', '-', 'o', '-', '-', '-', '-', '-', 'T']
        self.end = False
        
    def printBoard(self):
        print(np.array(self.span))

    def resetBoard(self):
        self.span = ['X', '-', '-', '-', '-', '-', 'o', '-', '-', '-', '-', '-', 'T']    
        
    def update(self, choice):
        i = self.getState()
        if choice == 0:
            self.span[i-1] = 'o'
            self.span[i] = '-'
        else:
            self.span[i+1] = 'o'
            self.span[i] = '-'
    
    def getState(self):
        return self.span.index('o')
    
    def check(self):
        if self.span.index('o') == 12:
            print("Finished! Success!")
            return 1
        elif self.span.index('o') == 0:
            print("Death by fire!")
            return -2
    
    def cend(self):
        if self.span.index('o') == 12 or self.span.index('o') == 0:
            self.end = True
        else:
            self.end = False

class Agent:
    
    def __init__(self):
        self.values = [-2, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1]
        self.history = []
        self.alpha = 0.01
    
    def takeAction(self, eps, state, env):
        
        if eps < np.random.random():
            if self.values[state-1] >= self.values[state+1]:
                env.update(0)
            else:
                env.update(1)
        else:
            temp = np.random.random()
            if temp > 0.5:
                env.update(0)
            else:
                env.update(1)
        self.history.append(state)
        env.cend()
    
    def resetHistory(self):
        self.history = []
    
    def update(self, env):
        reward = env.check()
        target = reward
        for prev in reversed(self.history):
          value = self.values[prev] + self.alpha*(target - self.values[prev])
          self.values[prev] = value
          target = value
        self.resetHistory()
            
env = Environment()
agent = Agent()
from os import system
for episode in range(100):
    while env.end == False:
        env.printBoard()
        agent.takeAction(0.1, env.getState(), env) 
    agent.update(env)
    env.resetBoard()
    env.cend()
