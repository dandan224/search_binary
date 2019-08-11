solution #1:
time complexity: O(n + logn)
class Solution(object):
  def shiftPosition(self, array):
    """
    input: int[] array
    return: int
    """
    # write your solution here
    if not array or len(array) == 0:
      return -1
    target = min(array)
    
    left, right = 0, len(array) - 1
    while left <= right:
      mid = int((left + right)/2)
      if array[mid] == target:
        return mid
      else:
        if array[left] <= array[mid] and array[left] > target:
          left = mid + 1
        else:
          right = mid - 1

Solution #2(binary search O(logn))

