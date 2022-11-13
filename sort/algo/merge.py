import time

class algorithm():
    def __init__(self) -> None:
        self.numberList = []
        self.swap = 0
        self.check = 0
        self.time = -1
    
    def setup(self, numberList: list[int]=None) -> None:
        if (numberList != None):
            self.numberList = numberList
    
    def countAction(self, isTest: bool=False, swap=False) -> None:
        if not isTest:
            if swap:
                self.swap += 1
            self.check += 1

    def mergeSort(self, numberList: list[int]) -> list[int]:
        if (len(numberList) >= 2):
            middle = int(len(numberList) / 2)
            left = self.mergeSort(numberList[:middle])
            right = self.mergeSort(numberList[middle:])
            res = []
            while (len(left) + len(right) > 0):
                isSwap = False
                if (len(left) == 0):
                    res.append(right.pop(0))
                elif (len(right) == 0):
                    res.append(left.pop(0))
                elif (left[0] < right[0]):
                    res.append(left.pop(0))
                else:
                    res.append(right.pop(0))
                    isSwap = True
                self.countAction(swap=isSwap)
            return res
        return numberList
  
    def run(self, isTest: bool=False) -> None:
        if not isTest:
            self.time = time.time()

            self.numberList = self.mergeSort(self.numberList)

            self.time = time.time() - self.time

    def print(self, isTest: bool=False) -> None:
        if not isTest:
            print(self.numberList)
            print("Swap: ", self.swap)
            print("Check: ", self.check)
            print("Time: ", self.time)
