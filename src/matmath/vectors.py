from math import pi, cos, sin, acos, sqrt

class Vector:
    def __init__(self, *args):
        """Creates a vector out of the given args."""
        if len(args) == 0:
            self.vector = [0, 0]
        elif len(args) == 1:
            if args[0] % 1 == 0 and args[0] > 0:
                self.vector = [0] * int(args[0])
            else:
                raise ValueError(f"The Vector cannot have {args[0]} dimensions. Number of dimensions must be a positive integer.")
        elif len(args) == 1 and type(args[0]) not in [int, float]:
            self.vector = list(args[0])
        elif len(args) > 1:
            self.vector = list(args)
        else:
            raise ValueError("Vector takes atleast 2 arguements only 1 given.")

    def __iter__(self):
        return self.vector.__iter__()

    def __len__(self):
        """returns the number of elements in the vector."""
        length = 0
        for _ in self.vector:
            length += 1
        return length

    def __setitem__(self, key, value):
        self.vector[key] = value

    def __getitem__(self, key):
        return self.vector[key]

    def __repr__(self):
        return '<' + str(self.vector)[1: -1] + '>'

    def __add__(self, other):
        """Adds 2 vectors of the same dimension.

        Parameters
        ----------
        other (Vector, compulsory)
            The second vector.

        Returns
        -------
        Vector
            Sum of 2 vectors.

        Raises
        ------
        ValueError
            Raised if the dimension of vectors are not equal.
        """
        if len(self) == len(other):
            ResultantVector = []
            for elem1, elem2 in zip(self, other):
                ResultantVector.append(elem1 + elem2)
            return Vector(ResultantVector)
        raise ValueError("The dimension of the 2 vectors must be the same.")

    def __sub__(self, other):
        """Subtracts 2 vectors of the same dimension.

        Parameters
        ----------
        other (Vector, compulsory)
            The second vector.
            
        Returns
        -------
        Vector
            Difference of 2 vectors.

        Raises
        ------
        ValueError
            Raised if the dimension of vectors are not equal.
        """
        if len(self) == len(other):
            ResultantVector = []
            for elem1, elem2 in zip(self, other):
                ResultantVector.append(elem1 - elem2)
            return Vector(ResultantVector)
        raise ValueError("The dimension of the 2 vectors must be the same.")

    def __mul__(self, other):
        """Returns the cross product of 2 vectors.

        Parameters
        ----------
        other (Vector, compulsory)
            The second vector.

        Returns
        -------
        Vector
            Cross product of the 2 vectors.

        Raises
        ------
        ValueError
            Raised if the dimension of vectors are not equal.
        ValueError
            Raised if the dimension of vectors is not equal to 2 or 3.
        """
        if self.__len__() == len(other):
            if self.__len__() == 3:
                a1, a2, a3 = self
                b1, b2, b3 = other
                return Vector([a2*b3 - a3*b2, a3*b1 + a1*b3, a1*b2 - a2*b1])
            elif self.__len__() == 2:
                a1, a2 = self
                b1, b2 = other
                return Vector([0, 0, a1*b2 - a2*b1])
            raise ValueError("The dimension of the 2 vectors must be less than or equal to 3.")
        raise ValueError("The dimension of the 2 vectors must be the same.")

    def __truediv__(self, number):
        """Divides the vector with the given number

        Args
        ----
        number (int/float): The number to divide.

        Returns
        -------
        Vector
            The vector divided with the given number.
        """
        if type(number) in [int, float]:
            divided = [i/number for i in self]
            return Vector(divided)
        else:
            TypeError("Only integer and float is allowed.")

    def __eq__(self, other):
        """Tells whether the vectors are equal or not.

        Parameters
        ----------
        other (Vector, compulsory)
            The second vector.

        Returns
        -------
        bool
            True if vectors are equal, False otherwise.
        """
        for i, j in zip(self, other):
            if i != j:
                return False
        return True

    def x(self):
        """Returns the first vector component."""
        return self[0]

    def y(self):
        """Returns the second vector component."""
        return self[1] if len(self) > 1 else 0

    def z(self):
        """Returns the third vector component."""
        return self[2] if len(self) > 2 else 0

    def w(self):
        """Returns the fourth vector component."""
        return self[3] if len(self) > 3 else 0

    def modulus(self):
        """Returns the modulus (length/magnitude) of the vector.

        Returns
        -------
        float
            magnitude of the length of the vector.
        """
        squared = 0
        for i in self:
            squared += i**2
        return sqrt(squared)

    def argument(self):
        """Returns the argument of the vector.

        Returns
        -------
        list
            a list containing angle which the vector makes with respect to the axes.
        """
        norm = self.modulus()
        return [acos(i / norm) for i in self]

    def unit_vector(self):
        """Returns the unit vector of the given vector.

        Returns
        -------
        Vector
            A vector of magnitude equal to 1 in the same direction as the given vector.
        """
        mod = self.modulus()
        UnitVector = []
        if mod == 0:
            return self
        for element in self:
            UnitVector.append(element / mod)
        return Vector(UnitVector)

    def magnify(self, magnification=1):
        """Returns the scaled-up or scaled-down version of the vector.

        Parameter
        ---------
        magnification (int/float, optional)
            The scale of magnification of the vector. Defaults to 1.

        Returns
        -------
        Vector
            A vector (whose magnitude = magnitude of original vector * magnification) in the same direction as the given vector.
        """
        NewVector = []
        for element in self.vector:
            NewVector.append(element * magnification)
        return Vector(NewVector)

    def rotate(self, theta=pi, radians=True):
        """Rotates the given vector by the given angle in clockwise direction.

        Parameters
        ----------
        theta (int/float, optional)
            The angle of rotation (in radians). Defaults to pi.
        radians (bool, optional)
            Unit of theta. radians (True) or degrees (False). Defaults to radians (True).

        Raises 
        ------
        ValueError
            Raised if the dimension of vector is not equal to 2.
        """
        if self.__len__() == 2:
            x = self.vector[0]
            y = self.vector[1]
            if not radians:
                theta = theta * pi / 180
            new_x = x * cos(theta) - y * sin(theta)
            new_y = x * sin(theta) + y * cos(theta)
            return Vector(new_x, new_y)
        raise ValueError("The dimension of the vector must be 2.")

    def dot_product(self, other):
        """The dot product of two vectors, if possible.

        Parameters
        ----------
        other (Vector, compulsory)
            The second vector.

        Returns
        -------
        Vector
            Dot product of the 2 vectors.

        Raises
        ------
        ValueError
            Raised if the dimension of vectors are not equal.
        """
        if len(self) == len(other):
            dotproduct = 0
            for elem1, elem2 in zip(self, other):
                dotproduct += elem1 * elem2
            return dotproduct
        raise ValueError("The dimension of the 2 vectors must be the same.")

    def cross_product(self, other):
        """The cross product of two vectors, if possible.

        Parameters
        ----------
        other (Vector, compulsory)
            The second vector.

        Returns
        -------
        Vector
            Cross product of the 2 vectors.

        Raises
        ------
        ValueError
            Raised if the dimension of vectors are not equal.
        ValueError
            Raised if the dimension of vectors is not equal to 2 or 3.
        
        Alias
        -----
            self.__mul__()
        """
        return self.__mul__(other)
    
    def is_unit(self):
        """Tells whether the vector is a unit or not.

        Returns
        -------
        bool
            True if the vector is a unit vector, False otherwise.
        """
        length = 0
        count_1 = 0
        count_0 = 0
        for i in self:
            length += 1
            if i == 0:
                count_0 +=1
            if i == 1:
                count_1 +=1
        return (count_1 == 1 and count_0 == (length - 1))
    
    def is_parellel(self, other):
        """Tells whether the vectors are parellel or not.

        Parameter
        ---------
        other (Vector, compulsory)
            The second vector.

        Returns
        -------
        bool
            True if the vectors are parellel, False otherwise.
        """
        ratio = self[0] / other[0]
        for i, j in zip(self, other):
            if i / j != ratio:
                return False
        return True
