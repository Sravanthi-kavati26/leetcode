class Solution:
    def maxArea(self, height: List[int]) -> int:
        area=0
        l=0
        r=len(height)-1
        while(l<r):
            length=min(height[l],height[r])
            breadth=r-l
            a=length*breadth
            area=max(area,a)
            if(height[l]<height[r]):
                l+=1
            else:
                r-=1
        return area
        