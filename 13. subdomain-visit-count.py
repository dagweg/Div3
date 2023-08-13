class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_map = {}
        for dom in cpdomains:
            dom = dom.split()
            ret = int(dom[0])
            dom = ''.join(dom[1:]).split('.')
            for i in range(len(dom)):
                keyy = '.'.join(dom[i:])
                if keyy in domain_map.keys():
                    domain_map[keyy] += ret
                else:
                    domain_map[keyy] = ret
        return [str(v)+' '+k for k,v in domain_map.items()]
