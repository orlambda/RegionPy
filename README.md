# RegionPy
Project to allow quick creation of navigable 2D and 3D grid-based regions for use in games made with RenPy. These regions can be added to a RenPy script so the entire game doesn't need to be grid-based.

This project is at the very start of its development.

## Scope
### Features:
- A Python program which generates a RenPy script to represent a 2D or 3D region with a given name and given dimensions, with a RenPy label correspending to each cell of the region's grid (e.g. "Room_X1_Y5_Z1").
- A Person/Being Python class (name TBC) for both PCs and NPCs which stores that person's location, and allows them to move, jumping them to the relevant scene according to location.
- A map image that can be shown and hidden with the "M" key during certain stages of the game (e.g. only within a particular region or if the player has found a map).

### Possible future features:
- Player/Person direction. Initially, XY will be the horizontal axes, as looking top-down or at a map. Z will likely be used for different floors/levels. As such, direction will be limited to the XY axes. The design will be such that this is easily changed according to usage. Each cell/direction combination may or may not need its own RenPy label.
- Generate default background images for each location (e.g. Room_X1_Y5_Z1.jpg).
- Allow multiple maps dependent on current region.
- Allow movement using keyboard (possibly using ESDF).
- Allow open/closed status of adjacent cells to be stored/amended, e.g. finding a key to open a door, using a directed graph in Python.
- Generate a default map image or other visual representation (may not be suitable for use in game but may be useful for developers to keep track of their regions).
- Expansion of Person/Being class to include character stats, levelling up, held/worn items, etc. This would be a part of a larger project/library that could include RegionPy.

## Use cases
- Dungeon crawlers, mazes, etc.
- Text adventures.
- Side-view instead of top down, e.g. moving through different rooms and floors of a building, showing a cross-section.
- Mini-games within traditional visual novels.

Created by Orlando Shamlou