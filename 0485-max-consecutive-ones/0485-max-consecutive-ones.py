class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        temp=0
        maxi=0
        for i in range(len(nums)):
            if nums[i]==1:
                temp+=1
            else:
                maxi=max(maxi,temp)
                temp=0
        if nums[-1]==1:
            maxi=max(temp,maxi)
        return maxi