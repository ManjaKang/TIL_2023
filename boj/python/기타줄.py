N, M = map(int, input().split())
p_arr = []
e_arr = []
for i in range(M):
    p, e = map(int, input().split())
    p_arr.append(p)
    e_arr.append(e)
p = min(p_arr)
e = min(e_arr)
answer = 0
if p >= e * 6:
    answer = N * e
else:
    answer += (N // 6) * p
    modN = N % 6
    answer += min(modN * e, p)
print(answer)