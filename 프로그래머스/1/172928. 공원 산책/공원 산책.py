def solution(park, routes):
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                x, y = i, j
                
    dx = {'E': 0, 'W': 0, 'S': 1, 'N': -1}
    dy = {'E': 1, 'W': -1, 'S': 0, 'N': 0}
    
    for route in routes:
        direction, steps = route.split()
        steps = int(steps)

        new_x, new_y = x, y
        valid = True

        for _ in range(steps):
            new_x += dx[direction]
            new_y += dy[direction]

            if not (0 <= new_x < len(park) and 0 <= new_y < len(park[0])) or park[new_x][new_y] == 'X':
                valid = False
                break

        if valid:
            x, y = new_x, new_y

    return [x, y]