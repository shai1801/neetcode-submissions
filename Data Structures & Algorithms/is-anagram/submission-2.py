class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charCountS={}
        charCountT={}
        indexS=0
        indexT=0
        while indexS < len(s):
            if s[indexS] in charCountS:
                charCountS[s[indexS]]+=1
            else:
                charCountS[s[indexS]]=1 
            
            indexS+=1

        while indexT < len(t):
            if t[indexT] in charCountT:
                charCountT[t[indexT]]+=1
            else:
                charCountT[t[indexT]]=1 

            indexT+=1

        if charCountS == charCountT:
            return True
        
        return False


        