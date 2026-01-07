class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # If list is empty
        if not strs:
            return ""

        #Take 1st string
        res = strs[0]

        for i in range(len(res)):
            #Check same char against same pos in other strings
            for j in range(1,len(strs)):
                #if we go beyond lenght of other string ir char doesn't match we return 
                if i>=len(strs[j]) or strs[j][i]!= res[i]:
                    return res[:i]

        return res      