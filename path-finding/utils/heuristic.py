class Heuristic:
    def Manhattan(start: tuple[int, int], goal: tuple[int, int]) -> float:
        return abs(start[0] - goal[0]) + abs(start[1] - goal[1])