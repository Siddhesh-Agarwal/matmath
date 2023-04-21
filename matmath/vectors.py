from math import acos, cos, pi, sin, sqrt
from typing import List, Union


class Vector:
    def __init__(self, *args: List[Union[int, float]]):
        __slots__ = "length", "__index"
        if len(args) == 0:
            self.vector = [0, 0]
        elif len(args) == 1:
            if isinstance(args[0], (int, float)):
                self.vector = [args[0]]
            else:
                for arg in args[0]:
                    if not isinstance(arg, (int, float)):
                        raise ValueError("Vector can contain only numbers.")
                self.vector = list(args[0])
        else:
            for arg in args:
                if not isinstance(arg, (int, float)):
                    raise ValueError("Vector can contain only numbers.")
            self.vector = list(args)
        self.length = len(self.vector)
        self.__index = 0

    def __iter__(self):
        """Makes the vector iterable"""
        return self.vector

    def __next__(self):
        """Returns the next iterator of the vector"""
        if self.__index < len(self.vector):
            self.__index += 1
            return self.vector[self.__index - 1]
        raise StopIteration

    def __len__(self):
        """returns the number of elements in the vector"""
        return self.length

    def __getitem__(self, key: int):
        """Returns the element at key in the vector"""
        return self.vector[key]

    def __repr__(self):
        """Returns a string construction of the vector"""
        return f"Vector({ str(self.vector)[1:-1] })"

    def __str__(self):
        """Returns a string representation of the vector"""
        return "<" + str(self.vector)[1:-1] + ">"

    def __add__(self, other):
        """Adds 2 vectors of the same dimension"""
        if self.length == len(other.vector):
            ResultantVector = []
            for elem1, elem2 in zip(self.vector, other.vector):
                ResultantVector.append(elem1 + elem2)
            return Vector(ResultantVector)
        raise TypeError("The dimension of the 2 vectors must be the same.")

    def __sub__(self, other):
        """Subtracts 2 vectors of the same dimension"""
        if self.length == len(other.vector):
            ResultantVector = []
            for elem1, elem2 in zip(self.vector, other.vector):
                ResultantVector.append(elem1 - elem2)
            return Vector(ResultantVector)
        raise TypeError("The dimension of the 2 vectors must be the same.")

    def __mul__(self, other):
        """Returns the product of vector and a number"""
        if isinstance(other, (int, float)):
            new = []
            for i in range(self.length):
                new.append(self.vector[i] * other)
            return Vector(new)
        elif isinstance(other, Vector):
            resultantVector = []
            for elem1, elem2 in zip(self.vector, other.vector):
                resultantVector.append(elem1 * elem2)
            return Vector(resultantVector)
        raise TypeError(f"Multiplication not supported between type Vector and type {type(other)}.")

    def __rmul__(self, other):
        """Returns the product of a number and a vector"""
        return self * other

    def __matmul__(self, other):
        """Matrix multiplication (cross product) of two vectors"""
        return self.cross_product(other)

    def __truediv__(self, number: Union[int, float]):
        """Divides the vector with the given number"""
        if isinstance(number, (int, float)):
            divided = [i / number for i in self]
            return Vector(divided)
        raise TypeError("can only divide by numbers.")

    def __eq__(self, other):
        """Tells whether the vectors are equal or not"""
        for i, j in zip(self, other):
            if i != j:
                return False
        return True

    def __ne__(self, other):
        """Tells whether the vectors are not equal"""
        return not self.__eq__(other)

    def __hash__(self):
        """Returns the hash of the vector"""
        return hash(tuple(self.vector))

    def __bool__(self):
        """Returns True if the vector is non-zero"""
        return sum(map(lambda x: x * x, self.vector)) != 0

    def __abs__(self):
        """Returns the modulus of the vector"""
        return self.modulus()

    def copy(self):
        """Returns a copy of the vector"""
        return Vector(self.vector)

    @staticmethod
    def modulus(self) -> float:
        """Returns the modulus (length/magnitude) of the vector

        Returns
        -------
        float
            magnitude of the length of the vector.
        """
        sum_of_squares = sum(map(lambda x: x * x, self.vector))
        return sqrt(sum_of_squares)

    @staticmethod
    def argument(self):
        """Returns the argument of the vector

        Returns
        -------
        list
            a list containing angle which the vector makes with respect to the axes.
        """
        norm = self.modulus()
        return [acos(i / norm) for i in self]

    def unit_vector(self):
        """Returns the unit vector of the given vector

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

    def magnify(self, magnification: Union[int, float] = 1):
        """Returns the scaled-up or scaled-down version of the vector

        Parameter
        ---------
        magnification (float, optional)
            The scale of magnification of the vector. Defaults to 1

        Returns
        -------
        Vector
            A vector (= vector * magnification) in the same direction as the given vector.
        """
        NewVector = []
        for element in self.vector:
            NewVector.append(element * magnification)
        return Vector(NewVector)

    def rotate(self, theta: Union[int, float] = pi, radians: bool = True):
        """Rotates the given vector by the given angle in clockwise direction

        Parameters
        ----------
        theta (int/float, optional)
            The angle of rotation (in radians). Defaults to pi.
        radians (bool, optional)
            Unit of theta. radians (True) or degrees (False). Defaults to radians (True).

        Returns
        -------
        Vector
            The vector rotated through the given angle in clockwise direction.

        Raises
        ------
        ValueError
            Raised if the dimension of vector is not equal to 2.
        """
        if self.length == 2:
            x = self.vector[0]
            y = self.vector[-1]
            if not radians:
                theta = theta * pi / 180
            new_x = x * cos(theta) - y * sin(theta)
            new_y = x * sin(theta) + y * cos(theta)
            rotated = [new_x, *self.vector[1:-1], new_y]
            return Vector(rotated)
        raise ValueError("The dimension of the vector must be equal to 2.")

    def dot_product(self, other):
        """The dot product of two vectors, if possible

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
        if self.length == len(other):
            dotproduct = 0
            for elem1, elem2 in zip(self, other):
                dotproduct += elem1 * elem2
            return dotproduct
        raise ValueError("The dimension of the 2 vectors must be the same.")

    def cross_product(self, other):
        """Returns the cross product of 2 vectors

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
        if self.length == len(other):
            if self.length == 3:
                a1, a2, a3 = self
                b1, b2, b3 = other
                return Vector([a2 * b3 - a3 * b2, a3 * b1 - a1 * b3, a1 * b2 - a2 * b1])
            elif self.length == 2:
                a1, a2 = self
                b1, b2 = other
                return Vector([0, 0, a1 * b2 - a2 * b1])
            raise ValueError("The dimension of the 2 vectors must be less than or equal to 3.")
        raise ValueError("The dimension of the 2 vectors must be the same.")

    @staticmethod
    def is_unit(self):
        """Tells whether the vector is a unit vector or not"""
        sum_of_squares = 0
        for i in self.vector:
            sum_of_squares += i**2
            if sum_of_squares > 1:
                return False
        return sum_of_squares == 1

    @staticmethod
    def is_parallel(self, other):
        """Tells whether the vectors are parallel or not"""
        ratio = self[0] / other[0]
        for i, j in zip(self, other):
            if i / j != ratio:
                return False
        return True

    @staticmethod
    def is_orthogonal(self, other):
        """Tells whether the vectors are orthogonal or not"""
        return self.dot_product(other) == 0

    @staticmethod
    def to_list(self):
        """Returns the vector as a list"""
        return self.vector

    @staticmethod
    def to_tuple(self):
        """Returns the vector as a tuple"""
        return tuple(self.vector)

    # Alias
    arg = argument
    mod = modulus
