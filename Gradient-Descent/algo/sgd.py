import time
import matplotlib.pyplot as plt
import numpy as np

class algorithm():
    def __init__(self) -> None:
        self.formula = None
    
    def setup(self, formula =None) -> None:
        if (formula != None):
            self.formula = formula
  
    def run(self, isTest: bool=False) -> None:
        if not isTest:
            self.time = time.time()
            
            # TO ADD

            self.time = time.time() - self.time

    def print(self, isTest: bool=False) -> None:
        if not isTest:
            arr = []
            for i in range(-100, 100, 1):
                arr.append(self.formula(i))    
            plt.plot(arr)
            plt.show()
