class Solution:
    def isHappy(self, n: int) -> bool:
        count = 0
        num = self.recurse(n)
        if n == 1: return True
        
        while count < 25:
            if num == 1: return True
            else:  count += 1
            num = self.recurse(num)
        return False

    def recurse(self, arr: int) -> int:
        total = 0
        string = str(arr)
        arr = list(string)

        for char in arr:
            total += int(char) ** 2

        return total