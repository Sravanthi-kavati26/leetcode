class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        res=[]
        res1=[]
        res2=[]
        for i in nums:
            if(i<pivot):
                res.append(i)
            elif(i==pivot):
                res1.append(i)
            else:
                res2.append(i)
        return res+res1+res2