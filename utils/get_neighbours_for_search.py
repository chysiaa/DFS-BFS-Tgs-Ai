from utils.get_neighbours import get_neighbours

def get_neighbours_for_search(maze, i, j, visited):
  
  partial_neighbours = get_neighbours(maze, i, j, visited)
  neighbours = []

  for neighbour in partial_neighbours:
    if neighbour[0] == i and neighbour[1] == j + 2 :
      if maze[i][j+1] == '1':
        neighbours.append(neighbour)
    elif neighbour[0] == i and neighbour[1] == j - 2:
      if maze[i][j-1] == '1':
        neighbours.append(neighbour)
    elif neighbour[0] == i + 2 and neighbour[1] == j:
      if maze[i+1][j] == '1':
        neighbours.append(neighbour)
    elif neighbour[0] == i - 2 and neighbour[1] == j:
      if maze[i-1][j] == '1':
        neighbours.append(neighbour)

  return neighbours