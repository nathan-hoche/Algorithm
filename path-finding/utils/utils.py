
class Node:
    def __init__(self, pos) -> None:
        self.pos = pos
        self.link = []
    
    def __repr__(self) -> str:
        return "Node:" + str(self.pos)

    def __str__(self) -> str:
        return "Node:" + str(self.pos)
    
    def setLink(self, ListNode: list[object]) -> None:
        LinkToAppend = [(self.pos[0], self.pos[1] + 1), (self.pos[0], self.pos[1] - 1), (self.pos[0] + 1, self.pos[1]), (self.pos[0] - 1, self.pos[1])]

        for node in LinkToAppend:
            for node2 in ListNode:
                if node2.isEqual(point=node):
                    self.link.append(node2)
                    break
    
    def isEqual(self, node:object = None, point:tuple[int, int] = None) -> bool:
        if node != None:
            return self.pos == node.pos
        elif point != None:
            return self.pos == point
        return False

class Convert:
    def convertMatrixToGraph(matrix: list[list[int]]) -> Node:
        graph = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    graph.append(Node((i, j)))
        for i in range(len(graph)):
            graph[i].setLink(graph)
        return graph

class Format:
    def formatMatrix(firstStart: tuple[int, int], end: tuple[int, int], matrix: list[list[int]], moveDone: list[list[int]]) -> list[list[str]]:
        for move in moveDone:
            matrix[move[0]][move[1]] = '2'
        matrix[firstStart[0]][firstStart[1]] = "S"
        matrix[end[0]][end[1]] = "E"
        for line in matrix:
            for i in range(len(line)):
                if line[i] == 0:
                    line[i] = "-"
                elif line[i] == 1:
                    line[i] = "#"
        return matrix