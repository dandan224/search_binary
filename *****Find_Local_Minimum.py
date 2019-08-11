class Solution(object):
  def localMinimum(self, array):
    """
    input: int[] array
    return: int
    """
    # write your solution here
    if not array or len(array) == 0:
      return
    left, right = 0, len(array) - 1

    while left < right:
      mid = int((left+right)/2)
      if array[mid] > array[mid+1]:
        left = mid+1
      else:
        right = mid
    
    return right
