- Rename Being to unit
    - Python
    - README
- Allow directions and turning
    - Add direction variable to Unit
    - Add turn() to Unit
    - Change "UP" etc. to NESW (Up Down?) in Unit and all calls to Unit.move()
    - Find and update all that call .move()
    - Find and update all that call ^ callers of .move()
    - Add direction parameter to cell labels RegionPy.py
    - Add direction parameter 
    - Write function that outputs label name based on x y z direction
    - Add x-y-z-direction labelname function to:
        - RegionPy.py
        -  move() in Being.rpy
        - set() in Location.rpy
    - Change cell background image name to include direction

- See if menu can have different styles (for movement vs dialogue)
- Make unobtrusive player movement menu
- Remove main menu for testing
- Add start and end points
- Add an item that must be found
- Add a map
- Make a map function that shows map for the current region

- For future keymaps
    Cannot use these keys:
    a
    s
    d
    f
    h
    v
    return
    space
    (IJKL for movement)
    maybe use b and n for interaction, or , and . (m for map), u, o
