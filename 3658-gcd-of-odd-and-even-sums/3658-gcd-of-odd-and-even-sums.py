class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumodd=n*n
        sumeven=n*(n+1)
        while(sumodd!=0):
            sumeven,sumodd=sumodd,sumeven%sumodd
        return sumeven