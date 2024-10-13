# class Person
# def move_person

init python:

    # Person class for player, potential use for other characters
    class Person:
        def __init__(self, id, name):
            # Set name
            try:
                self.name = name
            except:
                raise ValueError
            self.id = id
            self.area = "beach"
            self.x = 10
            self.y = 10
            self.z = None


        def __str__(self):
            return self.name

        # Getters - always one argument
        @property
        def id(self):
            return self._id

        @property
        def name(self):
            return self._name

        @property
        def area(self):
            return self._area

        @property
        def x(self):
            return self._x

        @property
        def y(self):
            return self._y

        @property
        def z(self):
            return self._z

        # Setters - always two arguments
        @id.setter
        def id(self, id):
            self._id = id

        @name.setter
        def name(self, name):
            self._name = f"{name}"

        @area.setter
        def area(self, area):
            self._area = f"{area}"

        @x.setter
        def x(self, x):
            try:
                self._x = int(x)
            except:
                raise ValueError

        @y.setter
        def y(self, y):
            try:
                self._y = int(y)
            except:
                raise ValueError

        @y.setter
        def z(self, z):
            try:
                self._z = int(z)
            except:
                raise ValueError

    # Navigation function

    def move_person(person, direction):
        if direction == "N":
            person.y += 1
        elif direction == "E":
            person.x += 1         
        elif direction == "S":
            person.y -= 1         
        elif direction == "W":
            person.x -= 1           
        elif direction not in ("N", "E", "S", "W"):
            renpy.jump("pit")
        destination = f"{person.area}_{person.x}_{person.y}"
        # Only player movement should cause jump to new label
        if person.id == 0:
            if renpy.has_label(destination):
                renpy.jump(destination)
            else:
                renpy.jump("pit")

    def toggle_map():
        if renpy.get_screen("map"):
            # renpy.hide_screen("map") # doesn't work
            wef = 24 # arbitrary while function is optimised
        else:
            if player_has_map == True and allow_map_view == True:
                # renpy.show_screen("map") # for alternative implementation
                renpy.call_in_new_context("map_label")
