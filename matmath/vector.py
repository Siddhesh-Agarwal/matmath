"""A module to represent vectors in n-dimensional space."""

from math import acos, cos, pi, sin, sqrt
from typing import Any, List, Optional, Union


class Vector:
    """A class to represent a vector in n-dimensional space."""

    vector: List[float]
    length: int

    def __init__(self, arr: Optional[List[float]] = None):
        if arr is None:
            arr = [0, 0]
        for i in arr:
            if not isinstance(i, (int, float)):
                raise TypeError("All elements of the vector must be `int` or `float`.")
        self.vector = arr
        self.length = len(arr)

    def __len__(self) -> int:
        """returns the number of elements in the vector"""
        return self.length

    def __getitem__(self, key: int) -> float:
        """Returns the element at key in the vector"""
        return self.vector[key]

    def __repr__(self) -> str:
        """Returns a string construction of the vector"""
        return f"Vector({str(self.vector)[1:-1]})"

    def __str__(self) -> str:
        """Returns a string representation of the vector"""
        return "<" + str(self.vector)[1:-1] + ">"

    def __add__(self, other: "Vector") -> "Vector":
        """Adds 2 vectors of the same dimension"""
        if not isinstance(other, self.__class__):
            raise ValueError("The second argument must be a vector.")
        if self.length == len(other.vector):
            result = [i + j for i, j in zip(self.vector, other.vector)]
            return Vector(result)
        raise TypeError("The dimension of the 2 vectors must be the same.")

    def __sub__(self, other: "Vector") -> "Vector":
        """Subtracts 2 vectors of the same dimension"""
        if not isinstance(other, self.__class__):
            raise ValueError("The second argument must be a vector.")
        if self.length == len(other.vector):
            result = [i - j for i, j in zip(self.vector, other.vector)]
            return Vector(result)
        raise TypeError("The dimension of the 2 vectors must be the same.")

    def __mul__(self, other: Union[int, float, "Vector"]) -> "Vector":
        """Returns the product of vector and a number"""
        if isinstance(other, (int, float)):
            result = [i * other for i in self.vector]
            return Vector(result)
        if isinstance(other, self.__class__):
            result = [i * j for i, j in zip(self.vector, other.vector)]
            return Vector(result)
        raise TypeError("The second argument must be a number or a vector.")

    def __rmul__(self, other: float) -> "Vector":
        """Returns the product of a number and a vector"""
        return self * other

    def __matmul__(self, other: "Vector") -> "Vector":
        """Matrix multiplication (cross product) of two vectors"""
        return self.cross_product(other)

    def __truediv__(self, other: Union[int, float, "Vector"]) -> "Vector":
        """Divides the vector with the given number"""
        if isinstance(other, (int, float)):
            result = [i / other for i in self.vector]
            return Vector(result)
        if isinstance(other, self.__class__):
            result = [i / j for i, j in zip(self.vector, other.vector)]
            return Vector(result)
        raise TypeError("The second argument must be a number or a vector.")

    def __eq__(self, other: Any) -> bool:
        """Tells whether the vectors are equal or not"""
        return isinstance(other, self.__class__) and self.vector == other.vector

    def __ne__(self, other: Any) -> bool:
        """Tells whether the vectors are not equal"""
        return not self.__eq__(other)

    def __hash__(self) -> int:
        """Returns the hash of the vector"""
        return hash(tuple(self.vector))

    def __bool__(self) -> bool:
        """Returns True if the vector is non-zero"""
        return any(self.vector)

    def __abs__(self) -> float:
        """Returns the modulus of the vector"""
        return self.modulus()

    def copy(self) -> "Vector":
        """Returns a copy of the vector"""
        return Vector(self.vector)

    def modulus(self) -> float:
        """Returns the modulus (length/magnitude) of the vector

        Returns
        -------
        float
            magnitude of the length of the vector.
        """
        sum_of_squares = sum(map(lambda x: x * x, self.vector))
        return sqrt(sum_of_squares)

    def argument(self) -> "Vector":
        """Returns the argument of the given vector

        Returns
        -------
        Vector
            A vector containing angle which the vector makes with respect to the axes.
        """
        norm = self.modulus()
        return Vector(list(map(lambda x: acos(x / norm), self.vector)))

    def unit_vector(self) -> "Vector":
        """Returns the unit vector of the given vector

        Returns
        -------
        Vector
            A vector of magnitude equal to 1 in the same direction as the given vector.
        """
        mod = self.modulus()
        if mod == 0:
            return Vector(self.vector)
        unit_vector = [ele / mod for ele in self.vector]
        return Vector(unit_vector)

    def magnify(self, magnification: float = 1) -> "Vector":
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
        new_vector = [ele * magnification for ele in self.vector]
        return Vector(new_vector)

    def rotate_2d(self, theta: float = pi, radians: bool = True) -> "Vector":
        """Rotates the given vector by the given angle in clockwise direction

        Parameters
        ----------
        theta (float, optional)
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
        if self.length != 2:
            raise ValueError("The dimension of the vector must be equal to 2.")
        x, y = self.vector
        if not radians:
            theta = theta * pi / 180
        new_x = x * cos(theta) - y * sin(theta)
        new_y = x * sin(theta) + y * cos(theta)
        return Vector([new_x, new_y])

    def rotate_3d(self, theta: float, axis: "Vector", radians: bool = True) -> "Vector":
        """Rotates the 3D vector around a given axis using Rodrigues' rotation formula.

        Parameters
        ----------
        theta : float
            The angle of rotation.
        axis : Vector
            The axis to rotate around.
        radians : bool, optional
            Whether theta is in radians or degrees. Defaults to True.

        Returns
        -------
        Vector
            The rotated 3D vector.

        Raises
        ------
        ValueError
            If the vector or the axis is not 3D.
        """
        if self.length != 3:
            raise ValueError("The dimension of the vector must be equal to 3.")

        if not radians:
            theta = theta * pi / 180

        # Rodrigues' rotation formula
        cos_t = cos(theta)
        sin_t = sin(theta)

        v_parallel = axis * (self.dot_product(axis))
        v_perp = self - v_parallel
        w = axis.cross_product(self)
        return v_parallel + v_perp * cos_t + w * sin_t

    def dot_product(self, other: "Vector") -> float:
        """The dot product of two vectors, if possible

        Parameters
        ----------
        other (Vector, compulsory)
            The second vector.

        Returns
        -------
        float
            Dot product of the 2 vectors.

        Raises
        ------
        ValueError
            Raised if the dimension of vectors are not equal.
        """
        if self.length == other.length:
            result = sum(
                elem1 * elem2 for elem1, elem2 in zip(self.vector, other.vector)
            )
            return result
        raise ValueError("The dimension of the 2 vectors must be the same.")

    def cross_product(self, other: "Vector") -> "Vector":
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
                a1, a2, a3 = self.vector
                b1, b2, b3 = other.vector
                return Vector([a2 * b3 - a3 * b2, a3 * b1 - a1 * b3, a1 * b2 - a2 * b1])
            elif self.length == 2:
                a1, a2 = self.vector
                b1, b2 = other.vector
                return Vector([0, 0, a1 * b2 - a2 * b1])
            raise ValueError(
                "The dimension of the 2 vectors must be less than or equal to 3."
            )
        raise ValueError("The dimension of the 2 vectors must be the same.")

    def is_unit(self) -> bool:
        """Tells whether the vector is a unit vector or not"""
        sum_of_squares = 0.0
        for i in self.vector:
            sum_of_squares += i**2
            if sum_of_squares > 1:
                return False
        return sum_of_squares == 1

    def is_parallel(self, other: "Vector") -> bool:
        """Tells whether the vectors are parallel or not"""
        ratio = self.vector[0] / other.vector[0]
        return all(i / j == ratio for i, j in zip(self.vector, other.vector))

    def is_orthogonal(self, other: "Vector") -> bool:
        """Tells whether the vectors are orthogonal or not"""
        return self.dot_product(other) == 0

    def to_list(self) -> List[float]:
        """Returns the vector as a list"""
        return self.vector

    # Alias
    arg = argument
    mod = modulus
    dot = dot_product
    cross = cross_product
