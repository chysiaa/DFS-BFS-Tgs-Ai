def get_neighbours(maze, i, j, visited):

  neighbours = []

  if i > 1 and [i-2, j] not in visited:
    neighbours.append([i-2, j])
  
  if i < len(maze)-2 and [i+2, j] not in visited:
    neighbours.append([i+2, j])

  if j > 1 and [i, j-2] not in visited:
    neighbours.append([i, j-2])

  if j < len(maze[0])-2 and [i, j+2] not in visited:
    neighbours.append([i, j+2])

  return neighbours