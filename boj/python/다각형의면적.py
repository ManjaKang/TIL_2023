N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]
temp = 0
arr = arr + [arr[0]]
for i in range(N):
    temp += arr[i][0] * arr[i+1][1] - arr[i+1][0] * arr[i][1]
print(round(abs(temp)/2, 1))