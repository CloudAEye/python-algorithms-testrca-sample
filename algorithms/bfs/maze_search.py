from collections import deque

'''
BFS time complexity : O(|E| + |V|)
BFS space complexity : O(|E| + |V|)

do BFS from (0,0) of the grid and get the minimum number of steps needed to get to the lower right column

only step on the columns whose value is 1

if there is no path, it returns -1

Ex 1)
If grid is
[[1,0,1,1,1,1],
 [1,0,1,0,1,0],
 [1,0,1,0,1,1],
 [1,1,1,0,1,1]], 
the answer is: 14

Ex 2)
If grid is
[[1,0,0],
 [0,1,1],
 [0,1,1]], 
the answer is: -1
'''

def maze_search(maze):
    """
    Maze search algorithm
    Args:
        maze: initial maze value

    Returns:

    """
    BLOCKED, ALLOWED = 0, 1
    UNVISITED, VISITED = 0, 1

    # Initialize x and y
    initial_x, initial_y = 0, 0

    # If maze is blocked return -1
    if maze[initial_x][initial_y] == BLOCKED:
        return -1

    # Initialize directions
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    # Define height and width of maze and targets
    height, width = len(maze), len(maze[0])
    target_x, target_y = height - 1, width - 1

    # Define a dequeue
    queue = deque([(initial_x, initial_y, 0)])

    # Track the visited nodes
    is_visited = [[UNVISITED for w in range(width)] for h in range(height)]
    # Mark this node as visited
    is_visited[initial_x][initial_y] = VISITED

    while queue:
        # Remove the first visited node
        x, y, steps = queue.popleft()

        # If target reached return steps
        if x == target_x and y == target_y:
            return steps

        # Define new directions
        for dx, dy in directions:
            new_x = x + dx # differential x
            new_y = y + dy

            # If new x and y are not within required height and width continue
            if not (0 <= new_x < height and 0 <= new_y < width):
                continue

            # Add to the queue and mark the node as visited
            if maze[new_x][new_y] == ALLOWED and is_visited[new_x][new_y] == UNVISITED:
                # append to the list
                queue.append((new_x, new_y, steps + 1))
                is_visited[new_x][new_y] = VISITED

    return -1 

