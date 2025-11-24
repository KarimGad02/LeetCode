# Last updated: 24/11/2025, 17:26:47
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map = {}
        memory = set()
        for i in range(len(s)):
            if s[i] in map:
                if map[s[i]] != t[i]:
                    return False
            else:
                if t[i] in memory:
                    return False
                map[s[i]] = t[i]
                memory.add(t[i])
        return True