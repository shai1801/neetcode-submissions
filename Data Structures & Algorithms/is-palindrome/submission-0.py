class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0,len(s)-1
        i=0

        while l<r:
            print(f"iteration no : {i}")
            while l<r and not self.alphaNum(s[l]):
                l+=1
            while r>l and not self.alphaNum(s[r]):
                r-=1
            print(f"l-char is {s[l]} and r-char is {s[r]}")
            if s[l].lower()!=s[r].lower():
                return False
            l, r = l+1, r-1
            i+=1
        return True

    def alphaNum(self,c):
        return (ord('A')<=ord(c)<=ord('Z') or
                ord('a')<=ord(c)<=ord('z') or
                ord('0')<=ord(c)<=ord('9'))

