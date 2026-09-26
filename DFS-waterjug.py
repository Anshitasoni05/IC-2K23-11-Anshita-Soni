def dfs(jug1, jug2, target):
    stack = [(0, 0)]
    visited = set()

    while stack:
        x, y = stack.pop()

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
                stack.append(state)

    print("Solution not possible")

dfs(4, 3, 2)

