import time
import matplotlib.pyplot as plt
import numpy as np

class algorithm():
    def __init__(self) -> None:
        self.formula = None
        self.pt = []
        self.value = []
    
    def setup(self, formula =None) -> None:
        if (formula != None):
            self.formula = formula
  
    def run(self, isTest: bool=False) -> None:
        if not isTest:
            self.time = time.time()
            
            # TO ADD
            vector = 45
            for _ in range(100):
                v = self.formula(vector)
                if v == 0:
                    break
                self.value.append(v)
                self.pt.append(vector)
                diff = -0.1 * np.array(v)
                vector += diff
            self.value.append(v)
            self.pt.append(self.formula(vector))

            self.time = time.time() - self.time

    def print(self, isTest: bool=False) -> None:
        if not isTest:
            arr = []
            for i in range(0, 100, 1):
                arr.append(self.formula(i))    
            plt.plot(arr, color='blue')
            plt.plot(self.pt, self.value, color='red', marker='o')
            plt.show()
