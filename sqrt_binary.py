https://leetcode.com/explore/learn/card/binary-search/125/template-i/950/
class Solution:
    def mySqrt(self, x: int) -> int:
        if x==1 or x==0:
            return x
        else: 
            l, r = 1, x//2
        while l<=r:
            m = (l+r)//2
            if m*m==x:
                return m
            elif m <= x/m:
                l = m+1
            elif m >= x/m:
                r = m-1
        return r
        
            
