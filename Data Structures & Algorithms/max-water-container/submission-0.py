class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i,j=0,len(heights)-1
        maxVol=0
        currVol=0
        while i<j:

            currVol=min(heights[i],heights[j])*(j-i)
            maxVol=max(currVol,maxVol)

            if(heights[i]<heights[j]):
                i+=1
            elif(heights[j]<heights[i]):
                j-=1
            else:
                i+=1
        return maxVol