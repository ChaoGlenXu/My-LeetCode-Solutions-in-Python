#1268. Search Suggestions System
#Medium
#problem statement:   https://leetcode.com/problems/search-suggestions-system/description/?envType=study-plan-v2&envId=leetcode-75

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
        self.suggestions = []

        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def build(self, products: List[str]):
        products.sort()
        
        for pro in products:
            cur = self.root
            for c in pro:
                if c not in cur.children: cur.children[c] = TrieNode()
                cur = cur.children[c]
                if len(cur.suggestions) < 3 : cur.suggestions.append(pro)
            cur.word = True

    def search (self, searchWord: str) -> List[List[str]]:
        res , len_sea = [], len(searchWord)
        cur = self.root

        for c in searchWord:
            if c not in cur.children: break
            cur = cur.children[c]
            res.append(cur.suggestions)

        while len(res) < len_sea: res.append([])

        return res     


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        #trie approach
        trie = Trie()
        trie.build(products)
        return trie.search(searchWord)

