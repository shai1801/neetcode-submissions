class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        
        res=[]
        l,r = 0,len(numbers)-1
        sum=numbers[l]+numbers[r]
        while sum!=target:
            sum = numbers[l]+numbers[r]
            if sum>target:
                r-=1
            elif sum<target:
                l+=1
        res.append(l+1)
        res.append(r+1)    
        return res

