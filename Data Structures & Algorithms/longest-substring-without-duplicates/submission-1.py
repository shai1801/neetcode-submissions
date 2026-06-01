class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ch = set()
        l,r=0,0
        res=0
        while r<len(s):
            if s[r] not in ch:
                ch.add(s[r])
                sz=r-l+1
                res=max(res,sz)
            else:
                ch.remove(s[l])
                l+=1
                continue
            r+=1
        return res
