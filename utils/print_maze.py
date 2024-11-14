def print_maze(maze):

    maze_copy = [row.copy() for row in maze]
    
    for i in range(len(maze_copy)):
        for j in range(len(maze_copy[0])):
            if maze_copy[i][j] == '0':
                maze_copy[i][j] = '🟥'
            elif maze_copy[i][j] == '1':
                maze_copy[i][j] = '🟨'
            elif maze_copy[i][j] == '2':
                maze_copy[i][j] = '🟩'

    return '\n'.join(''.join(row) for row in maze_copy)

