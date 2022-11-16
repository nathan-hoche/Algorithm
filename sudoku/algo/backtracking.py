import time

class algorithm():
    def __init__(self) -> None:
        self.map = []
        self.time = -1
    
    def setup(self, m: list[int]=None) -> None:
        if (m != None):
            self.map = m
    
    def checkIfPossible(self, x: int, y: int, n: int, map: list[int]) -> bool:
        if (n in map[x]):
            return False
        elif (n in [line[y] for line in map]):
            return False
        elif (n in [map[x - x % 3 + i][y - y % 3 + j] for i in range(3) for j in range(3)]):
            return False
        return True
    
    def backtracking(self, map: list[int]) -> list[int]:
        for x in range(len(map)):
            for y in range(len(map[x])):
                if (map[x][y] == 0):
                    for n in range(1, 10):
                        if (self.checkIfPossible(x, y, n, map)):
                            map[x][y] = n
                            if (self.backtracking(map) != None):
                                return map
                            map[x][y] = 0
                    return None
        return map

  
    def run(self, isTest: bool=False) -> None:
        if not isTest:
            self.time = time.time()
            self.map = self.backtracking(self.map)

            self.time = time.time() - self.time

    def print(self, isTest: bool=False) -> None:
        if not isTest:
            print("Possible Move:")
            x = 0
            for line in self.map:
                y = 0
                if (x % 3 == 0):
                    print("-------------------------")
                for i in line:
                    if (y % 3 == 0):
                        print("|", end=" ")
                    print(i, end=" ")
                    y += 1
                print("|")
                x += 1
            print("-------------------------")
            print("Time: ", self.time)
