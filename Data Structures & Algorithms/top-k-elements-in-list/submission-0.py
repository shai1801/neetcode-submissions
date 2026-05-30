class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers = {}
        for i in range(len(nums)):
            numbers[nums[i]] = numbers.get(nums[i],0)+1
        arr=[]
        for key, value in numbers.items():
            arr.append([value,key])
        arr.sort()
        res = []
        for i in range(k):
            res.append(arr.pop()[1])
        
       
        return res
