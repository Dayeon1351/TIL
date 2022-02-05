import sys
input = sys.stdin.readline

class Trie:
    def __init__(self):
        self.root = {}
    
    def add(self,foods):
        cur = self.root

        for food in foods:
            if food not in cur:
                cur[food] = {}
            cur = cur[food]
        
        cur[0] = True

    
    def search(self,level,cur):
        if 0 in cur:
            return
        cur_child = sorted(cur)

        for c in cur_child:
            print("--" * level + c)
            self.search(level + 1, cur[c])


n = int(input())
trie = Trie()
for _ in range(n):
    trie.add(input().split()[1:])

trie.search(0,trie.root)