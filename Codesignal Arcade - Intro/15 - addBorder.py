# https://app.codesignal.com/arcade/intro/level-4/ZCD7NQnED724bJtjN
def solution(picture):
    ans = ['e']*(len(picture)+2)
    ans[0] = ''.join(['*']*int(len(picture[0])+2))
    ans[len(picture)+1] = ''.join(['*']*int(len(picture[0])+2))
    for i in range(len(picture)):
        ans[i+1] =  "*" + picture[i] + '*'
  
    return ans
  
  def solution2(picture):
    l=len(picture[0])+2
    return ["*"*l]+[x.center(l,"*") for x in picture]+["*"*l]
