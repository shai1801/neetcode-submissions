class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tLen=len(temperatures)
        res=[]
        
        for i in range(tLen-1):
            count=1
            for j in range(i+1,tLen):
                print(f"temp i is {temperatures[i]} temp j is {temperatures[j]}")
                if temperatures[j]<=temperatures[i]:
                    count+=1
                else:
                    break
                count=0 if j==tLen-1 else count
            res.append(count)
            count=0
        res.append(0)
        return res
