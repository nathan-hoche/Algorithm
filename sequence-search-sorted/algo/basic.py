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
  
    def run(self, isTest: bool=False) -> None:
        if not isTest:
            self.time = time.time()
            
            for x in self.list:
                if x == self.objectif:
                    self.found = True
                    break
            self.time = time.time() - self.time

    def print(self, isTest: bool=False) -> None:
        if not isTest:
            #print("List: ", self.list)
            print("Size of list: ", len(self.list))
            print("Objectif: ", self.objectif)
            print("Found: ", self.found)
            print("Time: ", self.time)
