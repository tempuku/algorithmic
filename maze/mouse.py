from typing import *


class Solution:

    def solve_maze(self, maze: List[List[int]]):
        self.M = len(maze)
        self.N = len(maze[0])
        self.solve = [[0 for j in range(self.N)] for i in range(self.M)]
        self.maze = maze
        return self.help_util(0, 0)

    def help_util(self, x: int, y: int):
        if x == self.N - 1 and y == self.M - 1:
            self.solve[y][x] = 1
            return True
        if self.is_safe(x, y):
            self.solve[y][x] = 1
            if self.help_util(x + 1, y):
                return True
            if self.help_util(x, y + 1):
                return True
            self.solve[y][x] = 0
            return False
        return False

    def is_safe(self, x, y):
        if x < self.N and y < self.M and self.maze[y][x] != 1:
            return True
        return False


if __name__ == '__main__':
    maze = [
        [0, 1, 1, 1, 1],
        [0, 0, 1, 0, 0],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 0, 0],
        [1, 0, 1, 1, 1],
        [1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0],
        [1, 1, 1, 0, 0],
        [1, 1, 1, 1, 0],
    ]
    s = Solution()
    result = s.solve_maze(maze)
    print(s.solve)
