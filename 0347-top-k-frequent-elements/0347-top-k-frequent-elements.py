class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        first_index = 0
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else: count[num] = 1 
        
        sort = sorted(count, key=count.get, reverse=True) 
        return sort[:k]