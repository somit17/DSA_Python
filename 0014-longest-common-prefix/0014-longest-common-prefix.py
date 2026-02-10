#Implementing Trie Solution
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_last_word = False

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_last_word = True

    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
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
        '''
        
        if not strs:
            return ""

        for s in strs:
            self.insert(s)

        prefix = []
        node = self.root
        while len(node.children) == 1 and not node.is_last_word:
            char , next_node  =  next(iter(node.children.items()))
            prefix.append(char)
            node = next_node

        return "".join(prefix)