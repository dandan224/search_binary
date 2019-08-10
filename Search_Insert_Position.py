class Solution(object):
  def searchInsert(self, input, target):
    """
    input: int[] input, int target
    return: int
    """
    # write your solution here
    if not input:
      return 0
    left, right = 0, len(input) - 1
    while left <= right:
      mid = int((left + right)/2)
      if input[mid] < target:
        left = mid + 1
      else:
        right = mid - 1
    return left
