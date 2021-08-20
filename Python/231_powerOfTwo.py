class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
          if n > 0:
            x = (log10(n)/log10(2))
            return (x-int(x)) == 0
          return False