import time
import random

class algorithm():
    def __init__(self) -> None:
        self.graph = []
        self.start = (0, 0)
        self.end = (0, 0)
        self.result = []
        self.cost = 0
        self.time = -1
    
    def setup(self, graph: list[list[int]]=None, start:tuple[int, int]=None, end: tuple[int, int]=None) -> None:
        if (graph != None and start != None and end != None):
            self.graph = graph
            self.start = start
            self.end = end
            self.moveDone = []
            self.cost = 0
            self.time = -1
    
    def countCost(self, isTest=False, reverse=False) -> None:
        if not isTest:
            if reverse:
                self.cost -= 1
            else:
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
        if (len(moves) == 0):
            self.countCost(reverse=True)
            self.start = self.moveDone.pop()
            return self.randomMove()
        return moves[random.randint(0, len(moves) - 1)]

    def formatGraph(self, firstStart) -> list[list[int]]:
        for move in self.moveDone:
            self.graph[move[0]][move[1]] = '2'
        self.graph[firstStart[0]][firstStart[1]] = "S"
        self.graph[self.end[0]][self.end[1]] = "E"
        for line in self.graph:
            for i in range(len(line)):
                if line[i] == 0:
                    line[i] = "-"
                elif line[i] == 1:
                    line[i] = "#"

    def run(self, isTest=False):
        if not isTest:
            self.time = time.time()
            firstStart = self.start
            while (self.start != self.end):
                self.moveDone.append(self.start)
                self.countCost()
                self.start = self.randomMove()
            self.formatGraph(firstStart)
            self.time = time.time() - self.time

    def print(self, isTest=False) -> None:
        if not isTest:
            print(*self.graph, sep="\n")
            print("Cost: ", self.cost)
            print("Time: ", self.time)
