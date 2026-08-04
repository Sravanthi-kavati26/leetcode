class Solution:
    def maxPower(self, s: str) -> int:
        count=1
        maxi=0
        for i in range(1,len(s)):
            if s[i-1]==s[i]:
                count+=1
            else:
                maxi=max(count,maxi)
                count=1
        maxi=max(count,maxi)
        return maxi
            