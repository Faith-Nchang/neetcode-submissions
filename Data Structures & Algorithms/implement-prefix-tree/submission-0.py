class PrefixTree:

    def __init__(self):
        self.arr = []
        

    def insert(self, word: str) -> None:
        self.arr.append(word)


    def search(self, word: str) -> bool:
        for w in self.arr:
            if w == word:
                return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        n = len(prefix)
        for word in self.arr:
            if word[:n] == prefix:
                return True
        return False

        
        