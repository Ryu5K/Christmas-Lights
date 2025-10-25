# probably_a_fire_hazard.py

import json

def parse_instruction(line):
    """
    Parse a single instruction line.
    Returns (action, x1, y1, x2, y2)
    """
    parts = line.strip().split()
    if parts[0] == "toggle":
        action = "toggle"
        start = parts[1]
        end = parts[3]
    else:
        action = "on" if parts[1] == "on" else "off"
        start = parts[2]
        end = parts[4]
    x1, y1 = map(int, start.split(","))
    x2, y2 = map(int, end.split(","))
    return action, x1, y1, x2, y2


def apply_instruction(grid, action, x1, y1, x2, y2):
    """
    Apply an instruction to the grid.
    """
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if action == "on":
                grid[i][j] = True
            elif action == "off":
                grid[i][j] = False
            elif action == "toggle":
                grid[i][j] = not grid[i][j]


def count_lights_on(grid):
    """
    Count how many lights are on.
    """
    return sum(sum(1 for cell in row if cell) for row in grid)


def export_grid(grid, filename="grid.json"):
    """
    Export the current grid state, total on/off counts, and executed instructions
    for front-end visualization.
    """
    lights_on = sum(sum(1 for cell in row if cell) for row in grid)
    total_lights = len(grid) * len(grid[0])
    lights_off = total_lights - lights_on

    # read instructions so the front end can display them
    with open("instructions.txt", "r") as f:
        instructions = [line.strip() for line in f if line.strip()]

    data = {
        "count_on": lights_on,
        "count_off": lights_off,
        "total": total_lights,
        "grid": grid,
        "instructions": instructions
    }

    import json
    with open(filename, "w") as f:
        json.dump(data, f)

    print(f"Grid exported: {lights_on} lights ON, {lights_off} lights OFF.")




def main():
    # Read instructions from the file
    with open("instructions.txt", "r") as f:
        instructions = [line.strip() for line in f if line.strip()]

    # Create grid (all lights off)
    grid = [[False] * 1000 for _ in range(1000)]

    # Process each instruction line
    for line in instructions:
        action, x1, y1, x2, y2 = parse_instruction(line)
        apply_instruction(grid, action, x1, y1, x2, y2)

    # Count how many lights are on at the end
    print("Lights on:", count_lights_on(grid))

    # Export grid for visualization
    export_grid(grid)


if __name__ == "__main__":
    main()


