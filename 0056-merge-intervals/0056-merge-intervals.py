class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        sort = sorted(intervals)
        length = len(sort)
        arr = [sort[0]]

        i = 1
        while i < length:
                if arr[-1][1] >= sort[i][0]: 
                    max = arr[-1][1]
                    if sort[i][1] > arr[-1][1]: 
                        max = sort[i][1]
                    arr[-1][1] = max
                else: 
                    arr.append(sort[i])
                i += 1

        return arr
