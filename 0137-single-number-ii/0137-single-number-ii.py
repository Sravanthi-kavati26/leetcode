class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d={}
        for i in range(len(nums)):
            if d.get(nums[i]):
                d[nums[i]]+=1
            else:
                d[nums[i]]=1
        for k,v in d.items():
            if v==1:
                return k 