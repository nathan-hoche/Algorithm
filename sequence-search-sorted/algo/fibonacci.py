import time

class algorithm():
    def __init__(self) -> None:
        self.list = []
        self.objectif = -1
        self.found = False
        self.time = -1
    
    def setup(self, info: dict=None) -> None:
        if (info != None):
            self.list = info["list"]
            self.objectif = info["objectif"]

    def fibonacci(self, n: int, value1:int=0, value2:int=1) -> int:
        if value2 > n:
            return value2 - value1, value1, value2
        value3 = value1 + value2
        return self.fibonacci(n, value2, value3)
  
    def run(self, isTest: bool=False) -> None:
        if not isTest:
            self.time = time.time()
            
            ln = len(self.list)
            offset = -1
            v1, v2, v3 = self.fibonacci(ln)
            while (v3 > 1):
                i = min(offset + v2, ln - 1)

                if (self.list[i] < self.objectif):
                    v3 = v2
                    v2 = v1
                    v1 = v3 - v2
                    offset = i
                elif (self.list[i] > self.objectif):
                    v3 = v1
                    v2 = v2 - v1
                    v1 = v3 - v2
                else:
                    self.found = True
                    self.index = i
                    break

            self.time = time.time() - self.time

    def print(self, isTest: bool=False) -> None:
        if not isTest:
            #print("List: ", self.list)
            print("Size of list:", len(self.list))
            print("Objectif:", self.objectif)
            print("Found:", self.found, "at index", self.index)
            print("Time:", self.time)
