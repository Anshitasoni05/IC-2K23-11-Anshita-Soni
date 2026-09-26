from collections import deque

def water_jug(capacity1, capacity2, target):
    visited = set()
    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))
        print(x, y)

        if x == target or y == target:
            print("Goal Reached!")
            return

        states = [
            (capacity1, y),  # Fill jug 1
            (x, capacity2),  # Fill jug 2
            (0, y),          # Empty jug 1
            (x, 0),          # Empty jug 2
            (x - min(x, capacity2 - y), 
             y + min(x, capacity2 - y)),  # Pour jug 1 into jug 2
            (x + min(y, capacity1 - x), 
             y - min(y, capacity1 - x))   # Pour jug 2 into jug 1
        ]

        for state in states:
            if state not in visited:
                queue.append(state)

    print("Solution not possible")

water_jug(4, 3, 2)


