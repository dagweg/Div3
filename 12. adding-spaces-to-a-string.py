# Time : 10min
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        j = 0
        ret = ''
        for i in range(len(s)):
            if j < len(spaces) and i == spaces[j]:
                ret += ' '
                j += 1
            ret += s[i]
        return ret
