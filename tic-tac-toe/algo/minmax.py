import time

class algorithm():
    def __init__(self) -> None:
        self.map = []
        self.possibleMove = []
        self.time = -1
    
    def setup(self, m: list[int]=None) -> None:
        if (m != None):
            self.map = m
    
    def checkWinner(self, board: list[list[int]]) -> int:
        if board[0][0] == board[1][1] == board[2][2] != 0:
            return -10 if board[0][0] == -1 else 10
        if board[0][2] == board[1][1] == board[2][0] != 0:
            return -10 if board[0][2] == -1 else 10
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != 0:
                return -10 if board[i][0] == -1 else 10
            if board[0][i] == board[1][i] == board[2][i] != 0:
                return  -10 if board[0][i] == -1 else 10
        return None
    
    def minmax(self, board: list[list[int]], depth: int, myTurn: bool) -> int:
        result = self.checkWinner(board)
        if result != None:
            return result + (depth if myTurn else -depth)

        best_score = -1000 if myTurn else 1000
        for y in range(len(board)):
            for x in range(len(board[y])):
                if board[y][x] == 0:
                    board[y][x] = 1 if myTurn else -1
                    score = self.minmax(board, depth + 1, not myTurn)
                    board[y][x] = 0
                    best_score = max(score, best_score) if myTurn else min(score, best_score)
        return best_score
    
    def find_best_move(self, board: list[list[int]]) -> int:
        best_score = -1000
        best_move = (-1, -1)
        for y in range(len(board)):
            for x in range(len(board[y])):
                if board[y][x] == 0:
                    board[y][x] = 1
                    score = self.minmax(board, 0, False)
                    self.possibleMove.append({"score": score, "move": (y, x)})
                    board[y][x] = 0
                    if score > best_score:
                        best_score = score
                        best_move = (y, x)
        return best_move
  
    def run(self, isTest: bool=False) -> None:
        if not isTest:
            self.time = time.time()

            y, x = self.find_best_move(self.map)
            self.map[y][x] = 1
            self.time = time.time() - self.time

    def print(self, isTest: bool=False) -> None:
        if not isTest:
            print("Possible Move:")
            self.possibleMove.sort(key=lambda x: x["score"], reverse=True)
            for move in self.possibleMove:
                print("Move:", move["move"], "\tscore:", move["score"])
            print(*self.map, sep="\n")
            print("Time: ", self.time)
