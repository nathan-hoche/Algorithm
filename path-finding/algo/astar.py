import time
from utils.utils import Format
from utils.utils import Convert
from utils.heuristic import Heuristic

class algorithm():
    def __init__(self) -> None:
        self.graph = []
        self.matrix = []
        self.start = (0, 0)
        self.end = (0, 0)
        self.result = []
        self.cost = 0
        self.time = -1
        self.moveDone = []
        self.movePossible = []
    
    def setup(self, matrix: list[list[int]]=None, start:tuple[int, int]=None, end: tuple[int, int]=None) -> None:
        if (matrix != None and start != None and end != None):
            self.graph = Convert.convertMatrixToGraph(matrix)
            self.matrix = matrix
            self.start = start
            self.end = end
    
    def countCost(self, isTest: bool=False) -> None:
        if not isTest:
            self.cost += 1

    def canBePossible(self, pos: tuple[int, int]) -> bool:
        for move in self.movePossible:
            if move["node"].pos == pos:
                return True
        return False

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
            print("Number of Nodes: ", len(self.graph))
            x = 0
            while currentNode.pos != self.end:
                x += 1
                self.countCost()
                self.moveDone.append(currentNode.pos)
                for node in currentNode.link:
                    if node.pos not in self.moveDone and not self.canBePossible(node.pos):
                        self.movePossible.append({"node": node, "g": g + 1, "h": Heuristic.Manhattan(node.pos, self.end)})
                if (len(self.movePossible) == 0):
                    self.result = "No path found"
                    break
                # Without personnal optimization: (Test all possibilities in plane case)
                # move = self.movePossible.index(min(self.movePossible, key=lambda x: x["h"] + x["g"]))
                # g = self.movePossible[move]["g"]

                # Optimization: (To perform best way in plane case)
                move = self.movePossible[0]
                i = 0
                x = 0
                for m in self.movePossible:
                    if (m['h'] + m["g"] < move["h"] + move["g"] or (m['h'] + m["g"] == move["h"] + move["g"] and m["g"] < move["g"])):
                        move = m
                        i = x
                    x += 1
                currentNode = self.movePossible.pop(i)["node"]
            
            self.graph = Format.formatMatrix(firstStart, self.end, self.matrix, self.moveDone)
            self.time = time.time() - self.time

    def print(self, isTest: bool=False) -> None:
        if not isTest:
            print(*self.graph, sep="\n")
            print("Cost: ", self.cost)
            print("Time: ", self.time)
