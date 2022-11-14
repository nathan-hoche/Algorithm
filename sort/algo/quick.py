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


    def partition(self, array, low, high):
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= pivot:
                i = i + 1
                self.countAction(swap=True)
                (array[i], array[j]) = (array[j], array[i])
            else:
                self.countAction()
        self.countAction(swap=True)
        (array[i + 1], array[high]) = (array[high], array[i + 1])
        return i + 1

    def quick_sort(self, array, low, high):
        if low < high:
            pi = self.partition(array, low, high)
            self.quick_sort(array, low, pi - 1)
            self.quick_sort(array, pi + 1, high)

    def run(self, isTest: bool=False) -> None:
        if not isTest:
            self.time = time.time()

            self.quick_sort(self.numberList, 0, len(self.numberList)-1)


            self.time = time.time() - self.time

    def print(self, isTest: bool=False) -> None:
        if not isTest:
            print(self.numberList)
            print("Swap: ", self.swap)
            print("Check: ", self.check)
            print("Time: ", self.time)
