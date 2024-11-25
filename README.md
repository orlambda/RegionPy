# RegionPy
## Project overview
### Description
Project to allow quick creation of navigable 2D and 3D grid-based regions for use in games made with RenPy. Regions can be added to any RenPy script, so the rest of the game does not need to be grid-based or use regions in any way. 

### Advantages
- Generating a RenPy script for a region saves time writing the many labels (cells).
- Player "movement" saves time linking the cells within a region.
- Using Python for player location and movement allows tidy, robust code.

### Scope
#### Current features
- A Python program which generates a RenPy script to represent a 2D or 3D region with a given name and given dimensions, with a RenPy label correspending to each cell of the region's grid (e.g. "Room_X1_Y5_Z1").
- A Person/Being Python class (name TBC) for both PCs and NPCs which stores that person's location, and allows them to move, jumping them to the relevant scene according to location.
- A map image that can be shown and hidden with the "M" key during certain stages of the game (e.g. only within a particular region or if the player has found a map).
- Allow movement between cells using IJKL keys.

#### Possible future features
- Allow adding to a region instead of overwriting the file
- Player/Person direction. Initially, XY will be the horizontal axes, as looking top-down or at a map. Z will likely be used for different floors/levels. As such, direction will be limited to the XY axes. The design will be such that this is easily changed according to usage. Each cell/direction combination may or may not need its own RenPy label.
- Generate default background images for each location (e.g. Room_X1_Y5_Z1.jpg).
- Add robust error checking for valid RenPy label names.
- Allow multiple maps dependent on current region.
- Allow open/closed status of adjacent cells to be stored/amended, e.g. finding a key to open a door, using a directed graph in Python.
- Generate a default map image or other visual representation (may not be suitable for use in game but may be useful for developers to keep track of their regions).
- Expansion of Person/Being class to include character stats, levelling up, held/worn items, etc. This would be a part of a larger project/library that could include RegionPy.

### Use cases
- Navigable areas within traditional visual novels.
- Dungeon crawlers, mazes, etc.
- Text adventures.
- Side-view instead of top down, e.g. moving through different rooms and floors of a building, showing a cross-section.
- Mini-games within traditional visual novels.

### Current state
This project is in early development. It is currently usable to create regions and allow movement but features will be added, and I expect to completely change much of the existing code, including renaming variables and functions and restructuring code.

Information on how to use RegionPy will be added, suitable for both beginners and experienced programmers.

## Using RegionPy

### Repo structure
- main/ contains the python file which creates a region, and a template for the content of each label within that region
- prototyping/ contains a RenPy game used for testing. This contains one game used for multiple prototypes to avoid needing multiple game folders. Change the start label of script.py to use a different prototype.

## Adding RegionPy to a game

## Axes
Regions have 3 axes, x, y, and z. 2D regions are just 3D regions with z of length 1, every cell having z as 0 by default.

In the prototypes, the x-axis is treated as North to South, the y-axis is treated as West to East, and the z-axis is treated as going from a higher position to a lower position. The x-y-axes therefore form the horizontal plane. If your game uses another view, such as a side view, you may prefer to treat x as top to bottom, y as left to right, and z as distance from the viewer. You may need to change elements of the code to suits the needs of your game.

Created by Orlando Shamlou
