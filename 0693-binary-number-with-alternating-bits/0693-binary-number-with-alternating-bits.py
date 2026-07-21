class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binary=[]
        while(n!=0):
            binary.append(n%2)
            n=n//2
            for i in range(1,len(binary)):
                if(binary[i-1]==binary[i]):
                    return False
        return True
