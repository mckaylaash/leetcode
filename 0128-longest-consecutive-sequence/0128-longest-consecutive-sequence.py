class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        sett = set(nums)
        sort = sorted(list(sett))
        count = 0
        max = 0

        print(sort)
        if len(sort) >= 1:
            count = 1
            max = 1
            for i in range(1, len(sort)):
                if sort[i] == (sort[i-1] + 1): 
                    count +=1
                    if count > max: max = count
                else: 
                    if count > max: max = count
                    count = 1
                print(count)
                print(max)
        return max



