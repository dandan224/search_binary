class Solution(object):
  def search(self, array, target):
    """
    input: int[] array, int target
    return: int
    """
    # write your solution here
    if not array or not target:
      return -1
    index = self.findMax(array)
    if array[index] == target:
      return index
    elif array[index] < target:
      return -1
    else:
      left1, left2 = 0, index + 1
      right1, right2 = index -1, len(array) - 1
      while left1 <= right1:
        mid1 = int((left1 + right1)/2)
        if array[mid1] < target:
          left1 = mid1 + 1
        elif array[mid1] > target:
          right1 = mid1 - 1
        else:
          return mid1
      while left2 <= right2:
        mid2 = int((left2 + right2)/2)
        if array[mid2] < target:
          right2 = mid2 - 1    
        elif array[mid2] > target:
          left2 = mid2 + 1
        else:
          return mid2
      return -1

      





  def findMax(self, array):
    if not array or len(array)==0:
      return array
    left, right = 0, len(array) - 1
    while left < right:
      mid = int((left + right)/2)
      if array[mid] < array[mid + 1]:
        left = mid + 1
      else:
        right = mid
    return right
  
