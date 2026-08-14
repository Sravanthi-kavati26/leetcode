class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res=[]
        for i in nums:
            temp=[]
            while(i>0):
                l_d=i%10
                temp.insert(0,l_d)
                i=i//10
            res.extend(temp)
        return res