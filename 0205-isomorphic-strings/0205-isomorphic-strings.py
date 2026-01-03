class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return True
        
        map_s,map_t={},{}

        for i in range(len(s)):
            ch_s=s[i]
            ch_t=t[i]
            #s -> t mapping
            if ch_s in map_s:
                if map_s[ch_s] != ch_t:
                    return False
            else:
                map_s[ch_s] = ch_t

            # t -> s mapping
            if ch_t in map_t:
                if map_t[ch_t] != ch_s:
                    return False
            else:
                map_t[ch_t] = ch_s

        return True