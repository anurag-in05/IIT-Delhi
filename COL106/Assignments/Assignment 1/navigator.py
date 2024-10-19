from maze import *
from exception import *
from stack import *
class PacMan:
    def __init__(self, grid : Maze) -> None:
        self.navigator_maze = grid.grid_representation
    def find_path(self, start, end):     

    # def local_moves(self, current_pos):
    #     x, y = current_pos
    #     local = []
    #     if x - 1 >= 0 and self.navigator_maze[x - 1][y] == 0:
    #         local.append((x - 1, y))
    #     if y + 1 <= len(self.navigator_maze[0]) - 1 and self.navigator_maze[x][y + 1] == 0:
    #         local.append((x, y + 1))
    #     if x + 1 <= len(self.navigator_maze) - 1 and self.navigator_maze[x + 1][y] == 0:
    #         local.append((x + 1, y))
    #     if y - 1 >= 0 and self.navigator_maze[x][y - 1] == 0:
    #         local.append((x, y - 1))
    #     return local
    

    # def find_path(self, start, end):
        # # Check if start or end positions are occupied by ghosts
        # if self.navigator_maze[start[0]][start[1]] == 1 or self.navigator_maze[end[0]][end[1]] == 1:
        #     raise PathNotFoundException
        # if start == end:
        #     lis = []
        #     lis.append(start)
        #     return lis
        
        # coordinates_path = Stack()
        # coordinates_path.push(start)
        # self.navigator_maze[start[0]][start[1]] = 1
        # end_found = False
        
        # while not coordinates_path.isEmpty():
        #     current_pos = coordinates_path.top()
        #     local = self.local_moves(current_pos)
        #     if end in local:
        #         coordinates_path.push(end)
        #         end_found = True
        #         break
        #     if len(local) != 0:
        #         coordinates_path.push(local[0])
        #         self.navigator_maze[local[0][0]][local[0][1]] = 1
        #     else:
        #         coordinates_path.pop()
        
        # if (end_found):
        #     ans = []
        #     while not coordinates_path.isEmpty():
        #         top_element = coordinates_path.top()
        #         ans.append(top_element)
        #         coordinates_path.pop()
        #         self.navigator_maze[top_element[0]][top_element[1]] = 0 
        #     return ans[::-1]
        # else:
        #     raise PathNotFoundException