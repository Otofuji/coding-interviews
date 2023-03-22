def compute_pond_sizes(land: list[list[int]]) -> list[int]:
    def dfs(row, col, visited):
        if row < 0 or col < 0 or row >= len(land) or col >= len(land[0]) or visited[row][col] or land[row][col] != 0:
            return 0
        visited[row][col] = True
        size = 1
        for i in range(-1, 2):
            for j in range(-1, 2):
                size += dfs(row+i, col+j, visited)
        return size
    
    visited = [[False for _ in range(len(land[0]))] for _ in range(len(land))]
    pond_sizes = []
    for row in range(len(land)):
        for col in range(len(land[0])):
            if not visited[row][col] and land[row][col] == 0:
                pond_sizes.append(dfs(row, col, visited))
    
    return pond_sizes
