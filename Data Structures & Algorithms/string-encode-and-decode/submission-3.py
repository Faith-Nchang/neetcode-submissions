class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for string in strs:
            s+=f"{len(string)}#{string}"
        return s

    def decode(self, s: str) -> List[str]:
        i = 0
        decoded = []

        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            lenght = int(s[i:j])

            start = j + 1
            end = start + lenght

            w = s[start:end]

            decoded.append(w)
            i = end
        return decoded
