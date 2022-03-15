"""Some people are standing in a row in a park. There are trees between them which cannot be moved.
Your task is to rearrange the people by their heights in a non-descending order without moving the trees.
People can be very tall!
Example:
- For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be sortByHeight(a) = [-1, 150, 160, 170, -1, -1, 180, 190]."""

def solution(a):
    p = []
    for i in a:
        if i==-1:
            continue
        else:
            p.append(i)

    p.sort(reverse=True)
    
    for i in range(len(a)):
        if a[i]==-1:
            continue
        else:
            a[i] = p.pop()
    
    return a 
  
  def solution2(a):
    people = sorted(filter(lambda x: x != -1, a))
    return [people.pop(0) if i != -1 else -1 for i in a]
