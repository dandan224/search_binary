class Solution(object):
  def search(self, matrix, target):
    """
    input: int[][] matrix, int target
    return: int[]
    """
    # write your solution here
    if not matrix:
      return None
    M, N = len(matrix), len(matrix[0])
    
    # search from left corner
    x = M - 1 
    y = 0
    while x >= 0 and x <= M -1 and y >= 0 and y <= N - 1:
      if matrix[x][y] == target:
        return [x, y]
      elif matrix[x][y] > target:
        x -= 1
      else:
        y += 1
    return [-1, -1]
