class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        total_count = 0
        substring_len = len(pref)
        #O(n) approach
        for word in words:
            word_pref = word[:substring_len]
            print(f"{word_pref}")
            if word_pref == pref:
                total_count+=1
        
        return total_count