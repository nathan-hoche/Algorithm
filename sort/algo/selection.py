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

            for i in range(len(self.numberList), 1, -1):
                current = self.numberList[0]
                for j in range(1, i):
                    if current < self.numberList[j]:
                        current = self.numberList[j]
                    self.countAction()
                current = self.numberList.index(current)
                if (current != i-1):
                    self.numberList[current], self.numberList[i-1] = self.numberList[i-1], self.numberList[current]
                    self.countAction(swap=True)

            self.time = time.time() - self.time

    def print(self, isTest: bool=False) -> None:
        if not isTest:
            print(self.numberList)
            print("Swap: ", self.swap)
            print("Check: ", self.check)
            print("Time: ", self.time)
