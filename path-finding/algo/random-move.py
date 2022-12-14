import time
import random
from utils.utils import Format

class algorithm():
    def __init__(self) -> None:
        self.graph = []
        self.start = (0, 0)
        self.end = (0, 0)
        self.result = []
        self.cost = 0
        self.time = -1
        self.moveDone = []
    
    def setup(self, graph: list[list[int]]=None, start:tuple[int, int]=None, end: tuple[int, int]=None) -> None:
        if (graph != None and start != None and end != None):
            self.graph = graph
            self.start = start
            self.end = end
    
    def countCost(self, isTest: bool=False) -> None:
        if not isTest:
            self.cost += 1
    
    def randomMove(self) -> tuple[int, int]:
        moves = []
        if (self.start[0] + 1 < len(self.graph) and self.graph[self.start[0] + 1][self.start[1]] != 1):
            moves.append((self.start[0] + 1, self.start[1]))
        if (self.start[0] - 1 >= 0 and self.graph[self.start[0] - 1][self.start[1]] != 1):
            moves.append((self.start[0] - 1, self.start[1]))
        if (self.start[1] + 1 < len(self.graph[0]) and self.graph[self.start[0]][self.start[1] + 1] != 1):
            moves.append((self.start[0], self.start[1] + 1))
        if (self.start[1] - 1 >= 0 and self.graph[self.start[0]][self.start[1] - 1] != 1):
            moves.append((self.start[0], self.start[1] - 1))
        return moves[random.randint(0, len(moves) - 1)]

    def run(self, isTest: bool=False) -> None:
        if not isTest:
            self.time = time.time()
            firstStart = self.start
            while (self.start != self.end):
                self.moveDone.append(self.start)
                self.countCost()
                self.start = self.randomMove()
            self.graph = Format.formatMatrix(firstStart, self.end, self.graph, self.moveDone)
            self.time = time.time() - self.time

    def print(self, isTest: bool=False) -> None:
        if not isTest:
            print(*self.graph, sep="\n")
            print("Cost: ", self.cost)
            print("Time: ", self.time)
