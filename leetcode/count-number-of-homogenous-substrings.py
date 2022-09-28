# https://youtu.be/I3BzhnS9MwA
class Solution:        
    def countHomogenous(self, s: str) -> int:
        mod = (10**9 + 7)
#         #slow method
#         l = list(s)
#         c = [1]
#         for i in range(1,len(l)):
#             count = 1
#             ch = l[i]
#             rl = l[:i]
#             rl = rl[::-1]
#             for j in rl:
#                 if j==ch:
#                     count=count+1
#                 else:
#                     break
            
#             c.append(count)
#         s = sum(c)
#         ans = s % mod
        summ = 0
        for x, y in groupby(s):
            # print('x: ', x)
            # print('y: ', list(y))
            n = len(list(y))
            c = n*(n+1)/2
            summ=summ+c
            
        # return ans
        return int(summ % mod)
