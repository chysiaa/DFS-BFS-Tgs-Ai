import numpy as np

def generate_grid(n, m, maze):

  maze = np.full((m, n), '0')
  
  for i in range(m):
    if i % 2 == 0:
      maze[i] = np.full(n, '0')
    else:
      for j in range(n):
        if j % 2 == 0:
          maze[i][j] = '0'
        else:
          maze[i][j] = '1'

  return maze