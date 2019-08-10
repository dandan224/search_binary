# need review
class Solution(object):
  def search(self, array, target):
    """
    input: int[] array, int target
    return: int
    """
    # write your solution here
    if not array or len(array) == 0:
      return -1
    left, right = 0, len(array) - 1
    while left <= right:
      mid = left + int((right - left)/2)
      if array[mid] == target:
        return mid
      elif array[mid] > target:
        if array[left] > target and array[left] <= array[mid]:
          left = mid + 1
        else:
          right = mid -1
      else:
        if array[right] < target and array[right] >= array[mid]:
          right = mid - 1
        else:
          left = mid + 1
    return -1
