# Time: 13 min
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) > len(s) : return False

        mps = {}
        mpt = {}

        for c in s:
            if c not in mps.keys(): mps[c] = 0
            else: mps[c] += 1
        for c in t:
            if c not in mpt.keys(): mpt[c] = 0
            else: mpt[c] += 1
        
        return mps == mpt
