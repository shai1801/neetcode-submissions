class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currP=0
        
        l,r=0,1
        maxP=0
        
        while r<len(prices):
            if prices[l]<prices[r]:
                maxP=max(maxP,(prices[r]-prices[l]))
            else:
                l=r
            
            r+=1
           

        print(l,r)
        return maxP