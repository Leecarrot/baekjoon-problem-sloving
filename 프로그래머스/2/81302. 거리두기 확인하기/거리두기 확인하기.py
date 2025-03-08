from collections import deque

def is_safe(place):
    dx = [0, 1, 0, -1]  # 상하좌우 이동
    dy = [1, 0, -1, 0]

    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':  # 사람이 앉아있는 경우
                queue = deque([(i, j, 0)])  # (행, 열, 거리)
                visited = [[False] * 5 for _ in range(5)]
                visited[i][j] = True

                while queue:
                    x, y, dist = queue.popleft()
                    
                    if dist >= 2:
                        continue  # 거리 2 초과는 탐색할 필요 없음

                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]

                        if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                            if place[nx][ny] == 'P':  # 거리두기 위반
                                return 0
                            elif place[nx][ny] == 'O':  # 빈 자리면 계속 탐색
                                queue.append((nx, ny, dist + 1))
                            visited[nx][ny] = True
    return 1

def solution(places):
    return [is_safe(place) for place in places]
                    
                    
                    