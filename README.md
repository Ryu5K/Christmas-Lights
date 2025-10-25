# Probably a Fire Hazard 🎄

A Python + HTML visualization of the "Probably a Fire Hazard" grid-light problem.

## Features
- Simulates a 1000×1000 grid of lights (on/off states)
- Executes `instructions.txt` commands
- Displays results in a visual grid via `index.html`
- Shows total number of lights on
- Lists each executed instruction

## How to Run Locally
```bash
# 1. Generate grid.json from Python
python Fire Hazard Project.py

# 2. Start a local web server
python -m http.server

# 3. Open in browser
http://localhost:8000/index.html
