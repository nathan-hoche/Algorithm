import time
import math

class algorithm():
    def __init__(self) -> None:
        self.list = []
        self.objectif = -1
        self.found = False
        self.index = -1
        self.time = -1
    
    def setup(self, info: dict=None) -> None:
        if (info != None):
            self.list = info["list"]
            self.objectif = info["objectif"]
  
    def run(self, isTest: bool=False) -> None:
        if not isTest:
            self.time = time.time()

            ln = len(self.list)
            step = int(math.sqrt(ln))
            # Found block where element is
            while (int(step) < ln and self.list[int(step)] <= self.objectif):
                step += step
                if (step >= ln):
                    self.found = True
                    break
            
            if (int(step) >= ln):
                step = ln - 1
            # Found in block
            while (self.list[int(step)] > self.objectif):
                step -= 1
            self.index = int(step)

            self.time = time.time() - self.time

    def print(self, isTest: bool=False) -> None:
        if not isTest:
            #print("List: ", self.list)
            print("Size of list:", len(self.list))
            print("Objectif:", self.objectif)
            print("Found:", self.found, "at index", self.index)
            print("Time:", self.time)
