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
            
            high = len(self.list) -1
            low = 0
            mid = 0

            while ((self.list[high] != self.list[low]) and (self.objectif >= self.list[low]) and (self.objectif <= self.list[high])):
                mid = int(low + ((self.objectif - self.list[low]) * (high - low) / (self.list[high] - self.list[low])))

                if (self.list[mid] < self.objectif):
                    low = mid + 1
                elif (self.objectif < self.list[mid]):
                    high = mid - 1
                else:
                    self.found = True
                    self.index = mid
                    break


            self.time = time.time() - self.time

    def print(self, isTest: bool=False) -> None:
        if not isTest:
            #print("List: ", self.list)
            print("Size of list:", len(self.list))
            print("Objectif:", self.objectif)
            print("Found:", self.found, "at index", self.index)
            print("Time:", self.time)
