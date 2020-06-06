import numpy as np

# chain has to be formed in a way that it creates a 3x3x3 cube
def dfs(coordinates={}, previousMoves=[], lastPos=(0,0,0), index=0):
    #print(previousMoves, list(coordinates.keys()), lastPos, index)
    if index == len(chain):
        return previousMoves
    length = chain[index]
    # first Move
    if not previousMoves:
        for direction in (np.array([1, 0, 0]), np.array([0, 1, 0]), np.array([0, 0, 1])):
            coordinates = {tuple(direction * i): 1 for i in range(length)}
            res = dfs(coordinates, [tuple(direction)], direction*(length-1), 1)
            if res:
                return res
    else:
        lastMove = previousMoves[-1]
        lastMoveNegative = (-i for i in lastMove)
        for move in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
            if move == lastMove or move == lastMoveNegative:
                continue
            newCoordinates = []
            npMove = np.array(move)
            for i in range(1, length):
                newCoordinates.append(tuple(lastPos + npMove*i))
            # all coordinates are unvisited and inside the boundaries
            if (
                all(coo not in coordinates for coo in newCoordinates) and 
                all(0 <= i < 3 for i in newCoordinates[-1])
                ):
                combined = {k: v for k, v in coordinates.items()}
                for coo in newCoordinates:
                    coordinates[coo] = 1
                res = dfs(combined, previousMoves + [move], newCoordinates[-1], index+1)
                if res:
                    return res

chain = [3, 3, 3, 3, 2, 2, 2, 3, 3, 2, 2, 3, 2, 3, 2, 2, 3]
print(dfs())
