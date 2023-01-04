class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        answer = strs[0]
        for str in strs[1:]:
            for i in range(len(str)):
                if i < len(answer) and answer[i] == str[i]:
                    continue
                else:
                    answer = str[:i]
                    break
        return answer