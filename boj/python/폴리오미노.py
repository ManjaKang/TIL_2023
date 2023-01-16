_str = input()
answer = ''
X_len = 0
dot_len = 0
for ch in _str:
    if ch == 'X':
        X_len += 1
        answer += '.' * dot_len
        dot_len = 0
    if ch == '.':
        dot_len += 1
        if X_len % 2 == 0:
            answer += (X_len // 4) * 'AAAA' + (X_len % 4 // 2) * 'BB'
        else:
            print(-1)
            break
        X_len = 0
else:
    if X_len % 2 == 0:
        answer += '.' * dot_len + (X_len // 4) * 'AAAA' + (X_len % 4 // 2) * 'BB'
        print(answer)
    else:
        print(-1)