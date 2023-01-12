N, M = map(int, input().split())
arr = [int(input()) for _ in range(M)]
arr.sort(reverse=True)
answer_p = 0
answer_t = 0
for i in range(N):
    if i >= len(arr):
        break
    if answer_t <= arr[i] * (i+1):
        answer_t = arr[i] * (i+1)
        answer_p = arr[i]
print(answer_p, answer_t)