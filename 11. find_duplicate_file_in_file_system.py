# Time: 30 mins Subs : 3
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        mp = {}
        for string in paths:
            string = string.split()
            directory = string[0]
            c, f = '', ''
            for sub in (string[1:]):
                sub = sub.split('(')
                f, c = sub[0], sub[1].rstrip(')')
                if c not in mp.keys():
                    mp[c] = [directory+'/'+f]
                else:
                    mp[c].append(directory+'/'+f)
                
        ret = []
        for v in mp.values():
            if len(v) > 1: ret.append(v)
        return ret
