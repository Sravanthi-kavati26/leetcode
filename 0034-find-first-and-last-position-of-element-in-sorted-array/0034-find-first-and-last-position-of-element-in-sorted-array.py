class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l1=0
        h1=len(nums)-1
        ans1=-1
        while(l1<=h1):
            mid1=(l1+h1)//2
            if nums[mid1]==target:
                ans1=mid1
                l1=mid1+1
            elif(nums[mid1]<=target):
                l1=mid1+1
            else:
                h1=mid1-1
        l2=0
        h2=len(nums)-1
        ans2=-1
        while(l2<=h2):
            mid2=(l2+h2)//2
            if nums[mid2]==target:
                ans2=mid2
                h2=mid2-1
            elif(nums[mid2]<=target):
                l2=mid2+1
            else:
                h2=mid2-1
        return [ans2,ans1]
                       