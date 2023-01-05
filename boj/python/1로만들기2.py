from collections import deque
N = int(input())
q = deque()
now = [N]

while now[0] != 1:
    if now[0] % 3 == 0:
        q.append([now[0]//3] + now)
    if now[0] % 2 == 0:
        q.append([now[0]//2] + now)
    q.append([now[0]-1]+now)
    now = q.popleft()
print(len(now)-1)
print(*now[::-1])