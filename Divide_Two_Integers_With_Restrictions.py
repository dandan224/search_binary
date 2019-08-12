class Solution(object):
  def divide(self, a, b):
    """
    input: int a, int b
    return: int
    """
    # write your solution here
    import math
    sign = 0
    if b == 0:
      return 2147483647 
    if a == 0:
      return 0
    
    if (a> 0 and b > 0) or (a <0 and b < 0):
      sign = 1
    else:
      sign = -1
    res = sign * self.dividehelper(abs(a), abs(b))

    return res

  def dividehelper(self, a, b):
    count = 0
    sum = b
    while sum <= a:
      sum += b
      count += 1
      
    return count
