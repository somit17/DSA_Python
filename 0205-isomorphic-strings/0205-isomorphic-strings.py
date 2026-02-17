class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        #s <--> t

        my_dict = {}
        used_values = set()

        for i in range(len(s)):
            key = s[i]
            value = t[i]
            #Step 1
            if key in my_dict:
                if my_dict[key]!= value:
                    return False
            else:
                if value in used_values:
                    return False
                my_dict[key] = value
                used_values.add(value)

        return True