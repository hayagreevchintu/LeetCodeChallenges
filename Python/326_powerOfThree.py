class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n > 0:
            x = (log10(n)/log10(3))
            return (x-int(x)) == 0
        return False