class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqueInt = set()
        for i in range(len(nums)):
            if nums[i] in uniqueInt:
                return True
            uniqueInt.add(nums[i])
        return False

        