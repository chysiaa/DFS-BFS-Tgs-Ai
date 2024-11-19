from flask import Flask, render_template, request
import time

# Utils
from utils.generate_grid import generate_grid
from utils.print_maze import print_maze
from utils.carve import carve
from utils.modify import modify

# Algorithms
from algorithms.dfs_maze_solver import dfs_maze_solver
from algorithms.bfs_maze_solver import bfs_maze_solver

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    execution_times = {}
    block_counts = {}
    maze_for_dfs = ""
    maze_for_bfs = ""

    if request.method == "POST":
        m = int(request.form.get('m', 11))  
        n = int(request.form.get('m', 11))  
    else:
        m = 11
        n = 11

    maze = generate_grid(n, m, [])
    carve(maze)
    
    start = [1, 1]
    end = [m-2, n-2]

    modify(maze, m, n)
    
    maze[start[0]][start[1]] = '🟦'  
    maze[end[0]][end[1]] = '🟪'     

    default_maze_str = print_maze(maze)
    maze_for_dfs = maze.copy()
    maze_for_bfs = maze.copy()
    
    # Run DFS solver
    start_time_dfs = time.time()
    dfs_maze_solver(maze_for_dfs, start, end)
    execution_times['DFS'] = "{:.11f}".format(time.time() - start_time_dfs)
    block_counts['DFS'] = len([cell for row in maze_for_dfs for cell in row if cell == '2'])

    # Run BFS solver
    start_time_bfs = time.time()
    bfs_maze_solver(maze_for_bfs, start, end)
    execution_times['BFS'] = "{:.11f}".format(time.time() - start_time_bfs)
    block_counts['BFS'] = len([cell for row in maze_for_bfs for cell in row if cell == '2'])
    maze_dfs_str = print_maze(maze_for_dfs)
    maze_bfs_str = print_maze(maze_for_bfs)

    return render_template("index.html", 
                           execution_times=execution_times,
                           block_counts=block_counts, 
                           maze_dfs=maze_dfs_str, 
                           maze_bfs=maze_bfs_str,
                           default_maze=default_maze_str)

if __name__ == "__main__":
    app.run(debug=True)