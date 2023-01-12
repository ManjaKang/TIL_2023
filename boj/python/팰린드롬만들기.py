from collections import defaultdict
import string
name = input()
count_dict = defaultdict(int)
for ch in name:
    count_dict[ch] += 1

odd_flag = False
failure = False
odd = ''
answer = ''
for ch in count_dict:
    if count_dict[ch] % 2:
        if odd_flag:
            failure = True
            break
        odd_flag = True
        odd = ch

if failure:
    print("I'm Sorry Hansoo")
else:
    for ch in string.ascii_uppercase:
        answer += ch * (count_dict[ch] // 2)
    answer += odd + answer[::-1]
    print(answer)
