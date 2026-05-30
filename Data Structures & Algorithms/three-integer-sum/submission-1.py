class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # res=set()
        # nums.sort()
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             if nums[i]+nums[j]+nums[k]==0:
        #                 temp=[nums[i],nums[j],nums[k]]
        #                 res.add(tuple(temp))
        # return [list(i) for i in res]
        nums.sort()
        count=defaultdict(int)
        for num in nums:
            count[num]+=1
        res=[]
        for i in range(len(nums)):
            count[nums[i]]-=1
            if i and nums[i-1]==nums[i]:
                continue
            for j in range(i+1,len(nums)):
                count[nums[j]]-=1
                if j-1>i and nums[j-1]==nums[j]:
                    continue
                target=-(nums[i]+nums[j])
                if count[target]>0:
                    res.append([nums[i],nums[j],target])
            for j in range(i+1,len(nums)):
                count[nums[j]]+=1
        return res