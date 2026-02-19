class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False

        charToWord = {}

        for i, (c, w) in enumerate(zip(pattern, words)):
            if c in charToWord:
                if words[charToWord[c]] != w:
                    return False
            else:
                # iterates atmost 26 times (a - z)
                for k in charToWord:
                    if words[charToWord[k]] == w:
                        return False
                charToWord[c] = i

        return True