from math import pi, cos, sin, atan, sqrt

class Vector:
    def __init__(self, *args):
        """Creates a vector out of the given args."""
        self.vector = args


    def __iter__(self):
        return self.vector.__iter__()


    def __len__(self):
        return len(self.vector)


    def __getitem__(self, key):
        return self.vector[key]


    def __repr__(self):
        return str(self.vector)


    def modulus(self):
        """Returns the modulus (length/magnitude) of the vector."""

        Squared = [i**2 for i in self.vector]
        return sqrt(sum(Squared))


    def argument(self):
        """Returns the argument of the vector.

        Raises: 
            ValueError: Raised if the dimension of vector is not equal to 2.    
        """

        if self.__len__() == 2:
            return atan(self.vector[1] / self.vector[0])
        raise ValueError("The dimension of the vector must be 2.")


    def unitVector(self):
        """Returns the unit vector in the direction of the given vector."""

        mod = self.modulus()
        UnitVector = []
        if mod == 0:
            return self
        for element in self.vector:
            UnitVector.append(element / mod)
        return UnitVector


    def magnify(self, magnification=1):
        """Returns the scaled up or scaled down version of the vector.

        Args:
            magnification (int/float, optional): The scale of magnification of the vector. Defaults to 1.
        """

        NewVector = []
        for element in self.vector:
            NewVector.append(element * magnification)
        return NewVector


    def rotate(self, theta=0, radians=True):
        """Rotates the given vector by the given angle in clockwise direction.

        Args:
            theta (int/float, optional): The angle of rotation (in radians). Defaults to 0.
            radians (bool, optional)   : Unit of theta. radians (True) or degrees (False). Defaults to True.

        Raises: 
            ValueError: Raised if the dimension of vector is not equal to 2.
        """

        if self.__len__() == 2:
            x = self.vector[0]
            y = self.vector[1]
            if not radians:
                theta = theta * 180 / pi
            new_x = x * cos(theta) - y * sin(theta)
            new_y = x * sin(theta) + y * cos(theta)
            return [new_x, new_y]
        raise ValueError("The dimension of the vector must be 2.")


    def dot_product(self, other):
        """Multiplies 2 vectors of the same dimension.

        Args:
            other (Vector, compulsory): The second vector.

        Raises:
            ValueError: Raised if the dimension of vectors are not equal.
        """

        if len(self) == len(other):
            dotproduct = 0
            for elem1, elem2 in zip(self, other):
                dotproduct += elem1 * elem2
            return dotproduct
        raise ValueError("The dimension of the 2 vectors must be the same.")


    def cross_product(self, other):
        """Returns the cross product of 2 vectors.

        Args:
            other (Vector, compulsory): The second vector

        Raises:
            ValueError: Raised if the dimension of vectors are not equal.
            ValueError: Raised if the dimension of vectors is not equal to 2 or 3.
        """
        if self.__len__() == len(other):
            if self.__len__() == 3:
                a1, a2, a3 = self
                b1, b2, b3 = other
                return [a2*b3 - a3*b2, a3*b1 + a1*b3, a1*b2 - a2*b1]
            elif self.__len__() == 2:
                a1, a2 = self
                b1, b2 = other
                return [0, 0, a1*b2 - a2*b1]
            raise ValueError("The dimension of the 2 vectors must be less than or equal to 3.")
        raise ValueError("The dimension of the 2 vectors must be the same.")


    def __add__(self, other):
        """Adds 2 vectors of the same dimension.

        Args:
            other (Vector, compulsory): The second vector.

        Raises:
            ValueError: Raised if the dimension of vectors are not equal.
        """

        if len(self) == len(other):
            ResultantVector = []
            for elem1, elem2 in zip(self, other):
                ResultantVector = elem1 + elem2
            return ResultantVector
        raise ValueError("The dimension of the 2 vectors must be the same.")


    def __sub__(self, other):
        """Subtracts 2 vectors of the same dimension.

        Args:
            other (Vector, compulsory): The second vector.

        Raises:
            ValueError: Raised if the dimension of vectors are not equal.
        """

        if len(self) == len(other):
            ResultantVector = []
            for elem1, elem2 in zip(self, other):
                ResultantVector = elem1 - elem2
            return ResultantVector
        raise ValueError("The dimension of the 2 vectors must be the same.")


    def __mul__(self, other):
        """Returns the cross product of 2 vectors.

        Args:
            other (Vector, compulsory): The second vector

        Raises:
            ValueError: Raised if the dimension of vectors are not equal.
            ValueError: Raised if the dimension of vectors is not equal to 2 or 3.

        Alias: 
            cross_product()
        """

        return self.cross_product(other)