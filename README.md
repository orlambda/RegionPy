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

#### Possible future features
- Allow adding to a region instead of overwriting the file
- Player/Person direction. Initially, XY will be the horizontal axes, as looking top-down or at a map. Z will likely be used for different floors/levels. As such, direction will be limited to the XY axes. The design will be such that this is easily changed according to usage. Each cell/direction combination may or may not need its own RenPy label.
- Generate default background images for each location (e.g. Room_X1_Y5_Z1.jpg).
- Add robust error checking for valid RenPy label names.
- Allow multiple maps dependent on current region.
- Allow movement using keyboard (possibly using ESDF).
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
- /main contains the python file which creates a region, and a template for the content of each label within that region
- /prototyping contains a RenPy game used for testing. this contains multiple prototypes. change the start label of script.py to use a different prototype. this avoids having a separate RenPy game folder for each prototype.
- /wizard\ DEMO\ game\ for\ regionpy contains the first prototype game I made. it is kept here for reference.

### Basic usage
TODO

Created by Orlando Shamlou
