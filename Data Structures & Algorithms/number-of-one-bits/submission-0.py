class Solution:
    def hammingWeight(self, n: int) -> int:
        n_bits = bin(n)

        res = 0
        for i in n_bits:
            if i == "1":
                res += 1
        return res
        