Interactive grid where users place start/end points and obstacles.

Visualize Dijkstra’s, A*, and DFS/BFS with color-coded steps.

Add maze-generation algorithms (e.g., Prim’s).
Why?: Demonstrates algorithms + UI skills.

Stretch Goal: Let users tweak heuristic weights for A*.

pathfinding-visualizer/
├── main.py            # Core logic
├── constants.py       # Colors, grid size
└── algorithms/        # Dijkstra, A*, etc.

Left-click adds walls (gray).

Right-click adds start (red) and end (green) nodes.

Pressing SPACE runs Dijkstra’s algorithm and shows the path.
