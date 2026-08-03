class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def built(string):
            res=[]
            for i in string:
                if i!="#":
                    res.append(i)
                elif res:
                    res.pop()
            return res
        return built(s)==built(t)