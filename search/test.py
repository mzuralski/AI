__author__ = 'Marcin'

def manhatanDistance(position1, position2):
    "The Manhattan distance heuristic for a PositionSearchProblem"
    xy1 = position1
    xy2 = position2
    return abs(xy1[0] - xy2[0]) + abs(xy1[1] - xy2[1])

