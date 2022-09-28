# https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/submissions/
class Solution:
    def minOperations(self, s: str) -> int:
        l = list(s)
        le = len(l)
        l1 = '01'*int(le/2) + '0'*int(le%2)
        l2 = '10'*int(le/2) + '1'*int(le%2)
        l1 , l2 = list(l1), list(l2)
       
        # cl1 = [1 for i,j in zip(l,l1) if i==j]
        # cl2 = [1 for i,j in zip(l,l2) if i==j]
        
        c1, c2 = 0, 0
        for i in range(len(l)):
            if l[i]!=l1[i]:
                c1=c1+1
            if l[i]!=l2[i]:
                c2= c2+1
            
        return min(c1, c2)
        # return min(sum(cl1),sum(cl2))
