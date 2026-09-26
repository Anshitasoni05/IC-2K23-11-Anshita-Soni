from collections import deque

def bfs(jug1, jug2, target):
    queue = deque([(0, 0)])
    visited = set()

    while queue:
        x, y = queue.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))
        print(x, y)

        if x == target or y == target:
            print("Goal Reached")
            return

        states = [
            (jug1, y),
            (x, jug2),
            (0, y),
            (x, 0),
            (x - min(x, jug2-y), y + min(x, jug2-y)),
            (x + min(y, jug1-x), y - min(y, jug1-x))
        ]

        for state in states:
            if state not in visited:
                queue.append(state)

    print("Solution not possible")

bfs(4, 3, 2)

