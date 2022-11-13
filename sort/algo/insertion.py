import time

class algorithm():
    def __init__(self) -> None:
        self.numberList = []
        self.swap = 0
        self.check = 0
        self.time = -1
    
    def setup(self, numberList: list[list[int]]=None) -> None:
        if (numberList != None):
            self.numberList = numberList
    
    def countAction(self, isTest: bool=False, swap=False) -> None:
        if not isTest:
            if swap:
                self.swap += 1
            self.check += 1
  
    def run(self, isTest: bool=False) -> None:
        if not isTest:
            self.time = time.time()
        
            for i in range(len(self.numberList) -1):
                self.countAction()
                j = i + 1
                switch = 0
                while (i + switch >= 0 and self.numberList[i + switch] > self.numberList[j + switch]):
                    self.numberList[i + switch], self.numberList[j + switch] = self.numberList[j + switch], self.numberList[i + switch]
                    print(self.numberList)
                    self.countAction(swap=True)
                    switch -= 1
                self.countAction()

            self.time = time.time() - self.time

    def print(self, isTest: bool=False) -> None:
        if not isTest:
            print(self.numberList)
            print("Swap: ", self.swap)
            print("Check: ", self.check)
            print("Time: ", self.time)
