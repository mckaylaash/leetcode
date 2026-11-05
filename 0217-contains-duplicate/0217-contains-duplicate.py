class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        deduplication = set(nums)
        if len(deduplication) == len(nums): return False
        return True