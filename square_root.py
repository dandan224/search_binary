class Solution(object):
  def sqrt(self, x):
    """
    input: int x
    return: int
    """
    # write your solution here
    if x == 0 or x == 1:
      return x
    left = 1
    right = x
    while left <= right:
      mid = int((left + right)/2)
      if mid * mid == x:
        return mid
      # store the mid when the mid * mid less than x
      elif mid * mid < x:
        left = mid + 1
        res = mid
      else:
        right = mid - 1
    return res
