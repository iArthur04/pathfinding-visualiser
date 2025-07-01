import heapq

def dijkstra(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    heap = [(0, start)]
    visited = set()
    path = {}

    while heap:
        cost, (row, col) = heapq.heappop(heap)
        if (row, col) == end:
            break
        if (row, col) in visited:
            continue
        visited.add((row, col))

        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] != 3 and (r, c) not in visited:
                heapq.heappush(heap, (cost + 1, (r, c)))
                path[(r, c)] = (row, col)

    # Reconstruct path
    if end in path:
        current = end
        while current != start:
            yield current  # Yield path nodes for animation
            current = path[current]