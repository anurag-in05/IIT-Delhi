class Maze:
    def __init__(self, m: int, n : int) -> None:
        self.m=m
        self.n=n
        self.grid_representation = []
        for row in range(m):
            grid_row = []
            for column in range(n):
                grid_row.append(0)
            self.grid_representation.append(grid_row)
    def add_ghost(self, x : int, y: int) -> None:
        self.grid_representation[x][y]=1
        pass
    def remove_ghost(self, x : int, y: int) -> None:
        self.grid_representation[x][y]=0
        pass
    def is_ghost(self, x : int, y: int) -> bool:
        return self.grid_representation[x][y]==1
    def print_grid(self) -> None:
        for i in range(self.m):
            print( " ".join(str(self.grid_representation[i][j] for j in range(self.n))))