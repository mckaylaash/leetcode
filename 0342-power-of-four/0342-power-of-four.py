class Solution:
    import math
    def isPowerOfFour(self, n: int) -> bool:
        if n >= 1:
            ret = math.log(n) / math.log(4.0)
            return ret.is_integer()
        return False


        