import heapq

def create_2d_array_from_file(filename):
    with open(filename, "r") as file:
        content = file.read()

    # Create the 2D array based on the number of rows and characters
    array = [list(row) for row in content.splitlines()]

    for i in range(len(array)):
        for j in range(len(array[0])):
            array[i][j] = int(array[i][j])


    return array

def dijkstra(grid, start, end, least, most):
    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    pq = [(0, *start, 0, 0)]

    while pq:
        curr_cost, x, y, px, py = heapq.heappop(pq)
        curr_node = (x, y)
        if curr_node == end:
            return curr_cost
        if (curr_node, px, py) in visited:
            continue
        visited.add((curr_node, px, py))

        i, j = curr_node
        for di, dj in {(1, 0), (-1, 0), (0, 1), (0, -1)} - {(px, py), (-px, -py)}:
            c = curr_cost
            for d in range(1, most+1):
                ni, nj = i + di*d, j + dj*d
                if 0 <= ni < rows and 0 <= nj < cols:
                    c += grid[ni][nj]
                    if d >= least:
                        heapq.heappush(pq, (c, ni, nj, di, dj))


grid = create_2d_array_from_file("day17_input.txt")
start = (0, 0)
end = (len(grid)-1, len(grid[0])-1)

print(dijkstra(grid, start, end, 1, 3))
print(dijkstra(grid, start, end, 4, 10))