import time
from utils.utils import Format
from utils.utils import Convert
from utils.heuristic import Heuristic

class algorithm():
    def __init__(self) -> None:
        self.graph = []
        self.start = (0, 0)
        self.end = (0, 0)
        self.result = []
        self.cost = 0
        self.time = -1
    
    def setup(self, matrix: list[list[int]]=None, start:tuple[int, int]=None, end: tuple[int, int]=None) -> None:
        if (matrix != None and start != None and end != None):
            self.graph = Convert.convertMatrixToGraph(matrix)
            self.matrix = matrix
            self.start = start
            self.end = end
            self.moveDone = []
            self.movePossible = []
            self.cost = 0
            self.time = -1
    
    def countCost(self, isTest: bool=False) -> None:
        if not isTest:
            self.cost += 1

    def run(self, isTest: bool=False) -> None:
        if not isTest:
            self.time = time.time()
            firstStart = self.start
            
            currentNode = None
            for node in self.graph:
                if node.isEqual(point=self.start):
                    currentNode = node
                    break
            g = 0
            while currentNode.pos != self.end:
                self.countCost()
                self.moveDone.append(currentNode.pos)
                for node in currentNode.link:
                    if node.pos not in self.moveDone and node.pos not in self.movePossible:
                        self.movePossible.append({"node": node, "g": g, "h": Heuristic.Manhattan(node.pos, self.end)})
                self.movePossible.sort(key=lambda x: x["g"] + x["h"])
                if (len(self.movePossible) == 0):
                    self.result = "No path found"
                    break
                currentNode = self.movePossible.pop(0)["node"]
                g += 1
            
            self.graph = Format.formatMatrix(firstStart, self.end, self.matrix, self.moveDone)
            self.time = time.time() - self.time

    def print(self, isTest: bool=False) -> None:
        if not isTest:
            print(*self.graph, sep="\n")
            print("Cost: ", self.cost)
            print("Time: ", self.time)
