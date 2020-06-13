from math import sin, cos


class Transformations:
    def __init__(self):
        """Inititalizer for the class
        ! Note: Under no circumstance should the origin and origin rotation be accessed or modified directly,
        use the property getters and setters for that purpose
        """
        self.origin_ = [0, 0]
        self.origin_rot = 0

    @property
    def originx(self):
        """ The getter for originx property of the object


        :return: The x coordinate of the new origin
        """
        return self.origin_[0]

    @originx.setter
    def originx(self, x):
        """ The setter for the orginx property of the object

        :param x: The new x coordinate for the origin
        :return: None
        """

        if type(x) in (int, float):
            self.origin_[0] = x
        else:
            raise ValueError("Expected an int or float but received {} instead".format(type(x)))

    @property
    def originy(self):
        """The getter for originy property of the object

        :return: The y coordinate of the origin
        """

        return self.origin_[1]

    @originy.setter
    def originy(self, y):
        """The setter for the orginy property of the object

        :param y: The new y coordinate for the origin
        :return: None
        """
        if type(y) in (int, float):
            self.origin_[1] = y
        else:
            raise ValueError("Expected an int or float but received {} instead".format(type(y)))

    @property
    def origin(self):
        """The getter for the origin of the object

        :return: The origin of the shifted coordinate system with respect to the old system
        """
        return [self.originx, self.originy]

    @origin.setter
    def origin(self, origin):
        """The setter for the origin of the object

        :param origin: The new origin for the shifted coordinate system with respect to the original system
        :return: None
        """
        try:
            val1, val2 = origin
        except ValueError:
            raise ValueError("Expected an iterable with two items")
        else:
            self.originx, self.originy = origin

    @property
    def axes_rotation(self):
        """The getter for the rotation of the axes of new coordinate system

        :return: The angle by which the axes have been shifted anticlockwise(in radian)
        """
        return self.origin_rot

    @axes_rotation.setter
    def axes_rotation(self, angle):
        """The setter for the rotation of the axes of the new coordinate system

        :param angle: The angle(radian) by which the axes have to be rotated anticlockwise
        :return: None
        """
        if type(angle) in (int, float):
            self.origin_rot = angle
        else:
            raise ValueError("Expected int or float but received {} instead".format(type(angle)))

    def transform(self, pos):
        """Transforms the given coordinate to the true origin of the system
        ! Note: Should be used only after the origin and the axes rotation of the object has been set, otherwise
        it will have no effect on the coordinates

        :param pos: The coordinates of the the point in the new coordinate system which have to be shifted to the true
        origin
        :return: The coordinate in a tuple shifted to the true origin
        """
        try:
            val1, val2 = pos
        except ValueError:
            raise ValueError("Expected an iterable with two items")
        else:
            x = pos[0] * cos(self.axes_rotation) - pos[1] * sin(self.axes_rotation)
            y = pos[0] * sin(self.axes_rotation) + pos[1] * cos(self.axes_rotation)

            return x + self.originx, y + self.originy

    def set_origin(self, pos):
        """Function to set the origin of the new coordinate system relative to the true origin of the system

        :param pos: The new origin of the system relative to the true origin
        :return: None
        """
        self.origin = pos

    def set_rotation(self, angle):
        """Function to set the axes rotation(radian) in the anticlockwise direction

        :param angle: The angle by which the axes are rotated(radian) in anticlockwise direction
        :return: None
        """
        self.axes_rotation = angle
