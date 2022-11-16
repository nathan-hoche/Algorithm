import time

class algorithm():
    def __init__(self) -> None:
        self.map = []
        self.time = -1
    
    def setup(self, m: list[int]=None) -> None:
        if (m != None):
            self.map = m

    def possibleNumber(self, x: int, y: int, map: list[int]) -> bool:
        possible = [x for x in range(1, len(map) + 1)]
        for case in map[x]:
            if (case in possible):
                possible.pop(possible.index(case))
        for line in map:
            if (line[y] in possible):
                possible.pop(possible.index(line[y]))
        for i in range(3):
            for j in range(3):
                r = map[x - x % 3 + i][y - y % 3 + j]
                if (r in possible):
                    possible.pop(possible.index(r))
        return possible
    
    
    def backtracking(self, map: list[int], actual:tuple[int, int]=(0, 0)) -> list[int]:
        while (actual[0] != len(map)):
            if (map[actual[0]][actual[1]] == 0):
                pn = self.possibleNumber(actual[0], actual[1], map)
                for n in pn:
                    map[actual[0]][actual[1]] = n
                    if (self.backtracking(map, actual) != None):
                        return map
                    map[actual[0]][actual[1]] = 0
                return None
            if (actual[1] + 1 >= len(map[0])):
                actual = (actual[0] + 1, 0)
            else:
                actual = (actual[0], actual[1] + 1)
        return map


    def run(self, isTest: bool=False) -> None:
        if not isTest:
            self.time = time.time()
            self.map = self.backtracking(self.map)
            self.time = time.time() - self.time

    def print(self, isTest: bool=False) -> None:
        if not isTest:
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
