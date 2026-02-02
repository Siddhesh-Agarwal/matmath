#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <math.h>
#include <structmember.h>

/* Vector object structure */
typedef struct {
    PyObject_HEAD
    double *data;
    Py_ssize_t length;
} VectorObject;

/* Forward declarations */
static PyTypeObject VectorType;

/* Helper function to create a new Vector */
static VectorObject* Vector_new_from_data(double *data, Py_ssize_t length) {
    VectorObject *self = (VectorObject *)VectorType.tp_alloc(&VectorType, 0);
    if (self != NULL) {
        self->data = (double *)PyMem_Malloc(length * sizeof(double));
        if (self->data == NULL) {
            Py_DECREF(self);
            return (VectorObject *)PyErr_NoMemory();
        }
        memcpy(self->data, data, length * sizeof(double));
        self->length = length;
    }
    return self;
}

/* Vector.__new__ */
static PyObject* Vector_new(PyTypeObject *type, PyObject *args, PyObject *kwds) {
    VectorObject *self;
    self = (VectorObject *)type->tp_alloc(type, 0);
    if (self != NULL) {
        self->data = NULL;
        self->length = 0;
    }
    return (PyObject *)self;
}

/* Vector.__init__ */
static int Vector_init(VectorObject *self, PyObject *args, PyObject *kwds) {
    PyObject *arr = NULL;
    static char *kwlist[] = {"arr", NULL};

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "|O", kwlist, &arr)) {
        return -1;
    }

    /* Default to [0, 0] if no argument provided */
    if (arr == NULL || arr == Py_None) {
        self->length = 2;
        self->data = (double *)PyMem_Malloc(2 * sizeof(double));
        if (self->data == NULL) {
            PyErr_NoMemory();
            return -1;
        }
        self->data[0] = 0.0;
        self->data[1] = 0.0;
        return 0;
    }

    /* Convert Python list to C array */
    if (!PyList_Check(arr)) {
        PyErr_SetString(PyExc_TypeError, "Argument must be a list");
        return -1;
    }

    Py_ssize_t length = PyList_Size(arr);
    if (length == 0) {
        PyErr_SetString(PyExc_ValueError, "List cannot be empty");
        return -1;
    }

    double *data = (double *)PyMem_Malloc(length * sizeof(double));
    if (data == NULL) {
        PyErr_NoMemory();
        return -1;
    }

    for (Py_ssize_t i = 0; i < length; i++) {
        PyObject *item = PyList_GetItem(arr, i);
        if (!PyFloat_Check(item) && !PyLong_Check(item)) {
            PyMem_Free(data);
            PyErr_SetString(PyExc_TypeError, "All elements of the vector must be `int` or `float`.");
            return -1;
        }
        data[i] = PyFloat_AsDouble(item);
    }

    /* Free old data if exists */
    if (self->data != NULL) {
        PyMem_Free(self->data);
    }

    self->data = data;
    self->length = length;
    return 0;
}

/* Vector.__dealloc__ */
static void Vector_dealloc(VectorObject *self) {
    if (self->data != NULL) {
        PyMem_Free(self->data);
    }
    Py_TYPE(self)->tp_free((PyObject *)self);
}

/* Vector.__len__ */
static Py_ssize_t Vector_length(VectorObject *self) {
    return self->length;
}

/* Vector.__getitem__ */
static PyObject* Vector_getitem(VectorObject *self, Py_ssize_t index) {
    if (index < 0 || index >= self->length) {
        PyErr_SetString(PyExc_IndexError, "Vector index out of range");
        return NULL;
    }
    return PyFloat_FromDouble(self->data[index]);
}

/* Vector.__repr__ */
static PyObject* Vector_repr(VectorObject *self) {
    PyObject *result = PyUnicode_FromString("Vector(");
    for (Py_ssize_t i = 0; i < self->length; i++) {
        PyObject *num = PyUnicode_FromFormat("%.10g", self->data[i]);
        PyObject *temp = PyUnicode_Concat(result, num);
        Py_DECREF(result);
        Py_DECREF(num);
        result = temp;
        
        if (i < self->length - 1) {
            PyObject *comma = PyUnicode_FromString(", ");
            temp = PyUnicode_Concat(result, comma);
            Py_DECREF(result);
            Py_DECREF(comma);
            result = temp;
        }
    }
    PyObject *paren = PyUnicode_FromString(")");
    PyObject *temp = PyUnicode_Concat(result, paren);
    Py_DECREF(result);
    Py_DECREF(paren);
    return temp;
}

/* Vector.__str__ */
static PyObject* Vector_str(VectorObject *self) {
    PyObject *result = PyUnicode_FromString("<");
    for (Py_ssize_t i = 0; i < self->length; i++) {
        PyObject *num = PyUnicode_FromFormat("%.10g", self->data[i]);
        PyObject *temp = PyUnicode_Concat(result, num);
        Py_DECREF(result);
        Py_DECREF(num);
        result = temp;
        
        if (i < self->length - 1) {
            PyObject *comma = PyUnicode_FromString(", ");
            temp = PyUnicode_Concat(result, comma);
            Py_DECREF(result);
            Py_DECREF(comma);
            result = temp;
        }
    }
    PyObject *bracket = PyUnicode_FromString(">");
    PyObject *temp = PyUnicode_Concat(result, bracket);
    Py_DECREF(result);
    Py_DECREF(bracket);
    return temp;
}

/* Vector.__add__ */
static PyObject* Vector_add(VectorObject *self, PyObject *other) {
    if (!PyObject_TypeCheck(other, &VectorType)) {
        PyErr_SetString(PyExc_ValueError, "The second argument must be a vector.");
        return NULL;
    }
    
    VectorObject *other_vec = (VectorObject *)other;
    if (self->length != other_vec->length) {
        PyErr_SetString(PyExc_TypeError, "The dimension of the 2 vectors must be the same.");
        return NULL;
    }
    
    double *result_data = (double *)PyMem_Malloc(self->length * sizeof(double));
    if (result_data == NULL) {
        return PyErr_NoMemory();
    }
    
    for (Py_ssize_t i = 0; i < self->length; i++) {
        result_data[i] = self->data[i] + other_vec->data[i];
    }
    
    VectorObject *result = Vector_new_from_data(result_data, self->length);
    PyMem_Free(result_data);
    return (PyObject *)result;
}

/* Vector.__sub__ */
static PyObject* Vector_sub(VectorObject *self, PyObject *other) {
    if (!PyObject_TypeCheck(other, &VectorType)) {
        PyErr_SetString(PyExc_ValueError, "The second argument must be a vector.");
        return NULL;
    }
    
    VectorObject *other_vec = (VectorObject *)other;
    if (self->length != other_vec->length) {
        PyErr_SetString(PyExc_TypeError, "The dimension of the 2 vectors must be the same.");
        return NULL;
    }
    
    double *result_data = (double *)PyMem_Malloc(self->length * sizeof(double));
    if (result_data == NULL) {
        return PyErr_NoMemory();
    }
    
    for (Py_ssize_t i = 0; i < self->length; i++) {
        result_data[i] = self->data[i] - other_vec->data[i];
    }
    
    VectorObject *result = Vector_new_from_data(result_data, self->length);
    PyMem_Free(result_data);
    return (PyObject *)result;
}

/* Vector.__mul__ */
static PyObject* Vector_mul(VectorObject *self, PyObject *other) {
    double *result_data = (double *)PyMem_Malloc(self->length * sizeof(double));
    if (result_data == NULL) {
        return PyErr_NoMemory();
    }
    
    if (PyFloat_Check(other) || PyLong_Check(other)) {
        /* Scalar multiplication */
        double scalar = PyFloat_AsDouble(other);
        for (Py_ssize_t i = 0; i < self->length; i++) {
            result_data[i] = self->data[i] * scalar;
        }
    } else if (PyObject_TypeCheck(other, &VectorType)) {
        /* Element-wise multiplication */
        VectorObject *other_vec = (VectorObject *)other;
        if (self->length != other_vec->length) {
            PyMem_Free(result_data);
            PyErr_SetString(PyExc_TypeError, "The dimension of the 2 vectors must be the same.");
            return NULL;
        }
        for (Py_ssize_t i = 0; i < self->length; i++) {
            result_data[i] = self->data[i] * other_vec->data[i];
        }
    } else {
        PyMem_Free(result_data);
        PyErr_SetString(PyExc_TypeError, "The second argument must be a number or a vector.");
        return NULL;
    }
    
    VectorObject *result = Vector_new_from_data(result_data, self->length);
    PyMem_Free(result_data);
    return (PyObject *)result;
}

/* Vector.__rmul__ */
static PyObject* Vector_rmul(VectorObject *self, PyObject *other) {
    return Vector_mul(self, other);
}

/* Vector.__truediv__ */
static PyObject* Vector_truediv(VectorObject *self, PyObject *other) {
    double *result_data = (double *)PyMem_Malloc(self->length * sizeof(double));
    if (result_data == NULL) {
        return PyErr_NoMemory();
    }
    
    if (PyFloat_Check(other) || PyLong_Check(other)) {
        /* Scalar division */
        double scalar = PyFloat_AsDouble(other);
        if (scalar == 0.0) {
            PyMem_Free(result_data);
            PyErr_SetString(PyExc_ZeroDivisionError, "Division by zero");
            return NULL;
        }
        for (Py_ssize_t i = 0; i < self->length; i++) {
            result_data[i] = self->data[i] / scalar;
        }
    } else if (PyObject_TypeCheck(other, &VectorType)) {
        /* Element-wise division */
        VectorObject *other_vec = (VectorObject *)other;
        if (self->length != other_vec->length) {
            PyMem_Free(result_data);
            PyErr_SetString(PyExc_TypeError, "The dimension of the 2 vectors must be the same.");
            return NULL;
        }
        for (Py_ssize_t i = 0; i < self->length; i++) {
            if (other_vec->data[i] == 0.0) {
                PyMem_Free(result_data);
                PyErr_SetString(PyExc_ZeroDivisionError, "Division by zero");
                return NULL;
            }
            result_data[i] = self->data[i] / other_vec->data[i];
        }
    } else {
        PyMem_Free(result_data);
        PyErr_SetString(PyExc_TypeError, "The second argument must be a number or a vector.");
        return NULL;
    }
    
    VectorObject *result = Vector_new_from_data(result_data, self->length);
    PyMem_Free(result_data);
    return (PyObject *)result;
}

/* Vector.modulus */
static PyObject* Vector_modulus(VectorObject *self, PyObject *Py_UNUSED(ignored)) {
    double sum_of_squares = 0.0;
    for (Py_ssize_t i = 0; i < self->length; i++) {
        sum_of_squares += self->data[i] * self->data[i];
    }
    return PyFloat_FromDouble(sqrt(sum_of_squares));
}

/* Vector.__abs__ */
static PyObject* Vector_abs(VectorObject *self) {
    return Vector_modulus(self, NULL);
}

/* Vector.dot_product */
static PyObject* Vector_dot_product(VectorObject *self, PyObject *other) {
    if (!PyObject_TypeCheck(other, &VectorType)) {
        PyErr_SetString(PyExc_TypeError, "Argument must be a Vector");
        return NULL;
    }
    
    VectorObject *other_vec = (VectorObject *)other;
    if (self->length != other_vec->length) {
        PyErr_SetString(PyExc_ValueError, "The dimension of the 2 vectors must be the same.");
        return NULL;
    }
    
    double result = 0.0;
    for (Py_ssize_t i = 0; i < self->length; i++) {
        result += self->data[i] * other_vec->data[i];
    }
    
    return PyFloat_FromDouble(result);
}

/* Vector.cross_product */
static PyObject* Vector_cross_product(VectorObject *self, PyObject *other) {
    if (!PyObject_TypeCheck(other, &VectorType)) {
        PyErr_SetString(PyExc_TypeError, "Argument must be a Vector");
        return NULL;
    }
    
    VectorObject *other_vec = (VectorObject *)other;
    if (self->length != other_vec->length) {
        PyErr_SetString(PyExc_ValueError, "The dimension of the 2 vectors must be the same.");
        return NULL;
    }
    
    if (self->length == 3) {
        double result_data[3];
        result_data[0] = self->data[1] * other_vec->data[2] - self->data[2] * other_vec->data[1];
        result_data[1] = self->data[2] * other_vec->data[0] - self->data[0] * other_vec->data[2];
        result_data[2] = self->data[0] * other_vec->data[1] - self->data[1] * other_vec->data[0];
        return (PyObject *)Vector_new_from_data(result_data, 3);
    } else if (self->length == 2) {
        double result_data[3] = {0.0, 0.0, 0.0};
        result_data[2] = self->data[0] * other_vec->data[1] - self->data[1] * other_vec->data[0];
        return (PyObject *)Vector_new_from_data(result_data, 3);
    } else {
        PyErr_SetString(PyExc_ValueError, "The dimension of the 2 vectors must be less than or equal to 3.");
        return NULL;
    }
}

/* Vector.__matmul__ */
static PyObject* Vector_matmul(VectorObject *self, PyObject *other) {
    return Vector_cross_product(self, other);
}

/* Vector.unit_vector */
static PyObject* Vector_unit_vector(VectorObject *self, PyObject *Py_UNUSED(ignored)) {
    PyObject *mod_obj = Vector_modulus(self, NULL);
    double mod = PyFloat_AsDouble(mod_obj);
    Py_DECREF(mod_obj);
    
    if (mod == 0.0) {
        /* Return copy of self if modulus is 0 */
        return (PyObject *)Vector_new_from_data(self->data, self->length);
    }
    
    double *result_data = (double *)PyMem_Malloc(self->length * sizeof(double));
    if (result_data == NULL) {
        return PyErr_NoMemory();
    }
    
    for (Py_ssize_t i = 0; i < self->length; i++) {
        result_data[i] = self->data[i] / mod;
    }
    
    VectorObject *result = Vector_new_from_data(result_data, self->length);
    PyMem_Free(result_data);
    return (PyObject *)result;
}

/* Vector.magnify */
static PyObject* Vector_magnify(VectorObject *self, PyObject *args, PyObject *kwds) {
    double magnification = 1.0;
    static char *kwlist[] = {"magnification", NULL};
    
    if (!PyArg_ParseTupleAndKeywords(args, kwds, "|d", kwlist, &magnification)) {
        return NULL;
    }
    
    double *result_data = (double *)PyMem_Malloc(self->length * sizeof(double));
    if (result_data == NULL) {
        return PyErr_NoMemory();
    }
    
    for (Py_ssize_t i = 0; i < self->length; i++) {
        result_data[i] = self->data[i] * magnification;
    }
    
    VectorObject *result = Vector_new_from_data(result_data, self->length);
    PyMem_Free(result_data);
    return (PyObject *)result;
}

/* Vector.rotate_2d */
static PyObject* Vector_rotate_2d(VectorObject *self, PyObject *args, PyObject *kwds) {
    double theta = M_PI;
    int radians = 1;
    static char *kwlist[] = {"theta", "radians", NULL};
    
    if (!PyArg_ParseTupleAndKeywords(args, kwds, "|dp", kwlist, &theta, &radians)) {
        return NULL;
    }
    
    if (self->length != 2) {
        PyErr_SetString(PyExc_ValueError, "The dimension of the vector must be equal to 2.");
        return NULL;
    }
    
    if (!radians) {
        theta = theta * M_PI / 180.0;
    }
    
    double cos_theta = cos(theta);
    double sin_theta = sin(theta);
    double x = self->data[0];
    double y = self->data[1];
    
    double result_data[2];
    result_data[0] = x * cos_theta - y * sin_theta;
    result_data[1] = x * sin_theta + y * cos_theta;
    
    return (PyObject *)Vector_new_from_data(result_data, 2);
}

/* Vector.rotate_3d */
static PyObject* Vector_rotate_3d(VectorObject *self, PyObject *args, PyObject *kwds) {
    double theta;
    PyObject *axis_obj;
    int radians = 1;
    static char *kwlist[] = {"theta", "axis", "radians", NULL};
    
    if (!PyArg_ParseTupleAndKeywords(args, kwds, "dO|p", kwlist, &theta, &axis_obj, &radians)) {
        return NULL;
    }
    
    if (self->length != 3) {
        PyErr_SetString(PyExc_ValueError, "The dimension of the vector must be equal to 3.");
        return NULL;
    }
    
    if (!PyObject_TypeCheck(axis_obj, &VectorType)) {
        PyErr_SetString(PyExc_TypeError, "Axis must be a Vector");
        return NULL;
    }
    
    VectorObject *axis = (VectorObject *)axis_obj;
    if (axis->length != 3) {
        PyErr_SetString(PyExc_ValueError, "The axis must be a 3D vector.");
        return NULL;
    }
    
    if (!radians) {
        theta = theta * M_PI / 180.0;
    }
    
    /* Rodrigues' rotation formula */
    double cos_t = cos(theta);
    double sin_t = sin(theta);
    
    /* v_parallel = axis * (self.dot_product(axis)) */
    double dot = 0.0;
    for (Py_ssize_t i = 0; i < 3; i++) {
        dot += self->data[i] * axis->data[i];
    }
    
    double v_parallel[3];
    for (Py_ssize_t i = 0; i < 3; i++) {
        v_parallel[i] = axis->data[i] * dot;
    }
    
    /* v_perp = self - v_parallel */
    double v_perp[3];
    for (Py_ssize_t i = 0; i < 3; i++) {
        v_perp[i] = self->data[i] - v_parallel[i];
    }
    
    /* w = axis.cross_product(self) */
    double w[3];
    w[0] = axis->data[1] * self->data[2] - axis->data[2] * self->data[1];
    w[1] = axis->data[2] * self->data[0] - axis->data[0] * self->data[2];
    w[2] = axis->data[0] * self->data[1] - axis->data[1] * self->data[0];
    
    /* result = v_parallel + v_perp * cos_t + w * sin_t */
    double result_data[3];
    for (Py_ssize_t i = 0; i < 3; i++) {
        result_data[i] = v_parallel[i] + v_perp[i] * cos_t + w[i] * sin_t;
    }
    
    return (PyObject *)Vector_new_from_data(result_data, 3);
}

/* Vector.argument */
static PyObject* Vector_argument(VectorObject *self, PyObject *Py_UNUSED(ignored)) {
    PyObject *mod_obj = Vector_modulus(self, NULL);
    double norm = PyFloat_AsDouble(mod_obj);
    Py_DECREF(mod_obj);
    
    double *result_data = (double *)PyMem_Malloc(self->length * sizeof(double));
    if (result_data == NULL) {
        return PyErr_NoMemory();
    }
    
    for (Py_ssize_t i = 0; i < self->length; i++) {
        result_data[i] = acos(self->data[i] / norm);
    }
    
    VectorObject *result = Vector_new_from_data(result_data, self->length);
    PyMem_Free(result_data);
    return (PyObject *)result;
}

/* Vector.is_unit */
static PyObject* Vector_is_unit(VectorObject *self, PyObject *Py_UNUSED(ignored)) {
    double sum_of_squares = 0.0;
    for (Py_ssize_t i = 0; i < self->length; i++) {
        sum_of_squares += self->data[i] * self->data[i];
        if (sum_of_squares > 1.0) {
            Py_RETURN_FALSE;
        }
    }
    if (fabs(sum_of_squares - 1.0) < 1e-10) {
        Py_RETURN_TRUE;
    }
    Py_RETURN_FALSE;
}

/* Vector.is_parallel */
static PyObject* Vector_is_parallel(VectorObject *self, PyObject *other) {
    if (!PyObject_TypeCheck(other, &VectorType)) {
        PyErr_SetString(PyExc_TypeError, "Argument must be a Vector");
        return NULL;
    }
    
    VectorObject *other_vec = (VectorObject *)other;
    if (self->length != other_vec->length) {
        Py_RETURN_FALSE;
    }
    
    if (other_vec->data[0] == 0.0) {
        PyErr_SetString(PyExc_ZeroDivisionError, "Cannot check parallel with zero component");
        return NULL;
    }
    
    double ratio = self->data[0] / other_vec->data[0];
    for (Py_ssize_t i = 1; i < self->length; i++) {
        if (other_vec->data[i] == 0.0) {
            if (self->data[i] != 0.0) {
                Py_RETURN_FALSE;
            }
        } else {
            if (fabs(self->data[i] / other_vec->data[i] - ratio) > 1e-10) {
                Py_RETURN_FALSE;
            }
        }
    }
    Py_RETURN_TRUE;
}

/* Vector.is_orthogonal */
static PyObject* Vector_is_orthogonal(VectorObject *self, PyObject *other) {
    PyObject *dot_obj = Vector_dot_product(self, other);
    if (dot_obj == NULL) {
        return NULL;
    }
    double dot = PyFloat_AsDouble(dot_obj);
    Py_DECREF(dot_obj);
    
    if (fabs(dot) < 1e-10) {
        Py_RETURN_TRUE;
    }
    Py_RETURN_FALSE;
}

/* Vector.copy */
static PyObject* Vector_copy(VectorObject *self, PyObject *Py_UNUSED(ignored)) {
    return (PyObject *)Vector_new_from_data(self->data, self->length);
}

/* Vector.to_list */
static PyObject* Vector_to_list(VectorObject *self, PyObject *Py_UNUSED(ignored)) {
    PyObject *list = PyList_New(self->length);
    if (list == NULL) {
        return NULL;
    }
    
    for (Py_ssize_t i = 0; i < self->length; i++) {
        PyObject *item = PyFloat_FromDouble(self->data[i]);
        if (item == NULL) {
            Py_DECREF(list);
            return NULL;
        }
        PyList_SET_ITEM(list, i, item);
    }
    
    return list;
}

/* Vector.__eq__ */
static PyObject* Vector_richcompare(VectorObject *self, PyObject *other, int op) {
    if (!PyObject_TypeCheck(other, &VectorType)) {
        if (op == Py_EQ) {
            Py_RETURN_FALSE;
        } else if (op == Py_NE) {
            Py_RETURN_TRUE;
        }
        Py_RETURN_NOTIMPLEMENTED;
    }
    
    VectorObject *other_vec = (VectorObject *)other;
    
    if (op == Py_EQ) {
        if (self->length != other_vec->length) {
            Py_RETURN_FALSE;
        }
        for (Py_ssize_t i = 0; i < self->length; i++) {
            if (self->data[i] != other_vec->data[i]) {
                Py_RETURN_FALSE;
            }
        }
        Py_RETURN_TRUE;
    } else if (op == Py_NE) {
        if (self->length != other_vec->length) {
            Py_RETURN_TRUE;
        }
        for (Py_ssize_t i = 0; i < self->length; i++) {
            if (self->data[i] != other_vec->data[i]) {
                Py_RETURN_TRUE;
            }
        }
        Py_RETURN_FALSE;
    }
    
    Py_RETURN_NOTIMPLEMENTED;
}

/* Vector.__hash__ */
static Py_hash_t Vector_hash(VectorObject *self) {
    PyObject *tuple = PyTuple_New(self->length);
    if (tuple == NULL) {
        return -1;
    }
    
    for (Py_ssize_t i = 0; i < self->length; i++) {
        PyObject *item = PyFloat_FromDouble(self->data[i]);
        if (item == NULL) {
            Py_DECREF(tuple);
            return -1;
        }
        PyTuple_SET_ITEM(tuple, i, item);
    }
    
    Py_hash_t hash = PyObject_Hash(tuple);
    Py_DECREF(tuple);
    return hash;
}

/* Vector.__bool__ */
static int Vector_bool(VectorObject *self) {
    for (Py_ssize_t i = 0; i < self->length; i++) {
        if (self->data[i] != 0.0) {
            return 0;  /* Not all zero, so return False (inverted logic from Python) */
        }
    }
    return 1;  /* All zero, so return True */
}

/* Method definitions */
static PyMethodDef Vector_methods[] = {
    {"modulus", (PyCFunction)Vector_modulus, METH_NOARGS, "Returns the modulus of the vector"},
    {"mod", (PyCFunction)Vector_modulus, METH_NOARGS, "Alias for modulus"},
    {"argument", (PyCFunction)Vector_argument, METH_NOARGS, "Returns the argument of the vector"},
    {"arg", (PyCFunction)Vector_argument, METH_NOARGS, "Alias for argument"},
    {"unit_vector", (PyCFunction)Vector_unit_vector, METH_NOARGS, "Returns the unit vector"},
    {"magnify", (PyCFunction)Vector_magnify, METH_VARARGS | METH_KEYWORDS, "Magnifies the vector"},
    {"rotate_2d", (PyCFunction)Vector_rotate_2d, METH_VARARGS | METH_KEYWORDS, "Rotates 2D vector"},
    {"rotate_3d", (PyCFunction)Vector_rotate_3d, METH_VARARGS | METH_KEYWORDS, "Rotates 3D vector"},
    {"dot_product", (PyCFunction)Vector_dot_product, METH_O, "Dot product"},
    {"dot", (PyCFunction)Vector_dot_product, METH_O, "Alias for dot_product"},
    {"cross_product", (PyCFunction)Vector_cross_product, METH_O, "Cross product"},
    {"cross", (PyCFunction)Vector_cross_product, METH_O, "Alias for cross_product"},
    {"is_unit", (PyCFunction)Vector_is_unit, METH_NOARGS, "Check if unit vector"},
    {"is_parallel", (PyCFunction)Vector_is_parallel, METH_O, "Check if parallel"},
    {"is_orthogonal", (PyCFunction)Vector_is_orthogonal, METH_O, "Check if orthogonal"},
    {"copy", (PyCFunction)Vector_copy, METH_NOARGS, "Returns a copy"},
    {"to_list", (PyCFunction)Vector_to_list, METH_NOARGS, "Convert to list"},
    {NULL}
};

/* Sequence methods */
static PySequenceMethods Vector_as_sequence = {
    (lenfunc)Vector_length,           /* sq_length */
    0,                                 /* sq_concat */
    0,                                 /* sq_repeat */
    (ssizeargfunc)Vector_getitem,     /* sq_item */
    0,                                 /* sq_slice */
    0,                                 /* sq_ass_item */
    0,                                 /* sq_ass_slice */
    0,                                 /* sq_contains */
};

/* Number methods */
static PyNumberMethods Vector_as_number = {
    (binaryfunc)Vector_add,           /* nb_add */
    (binaryfunc)Vector_sub,           /* nb_subtract */
    (binaryfunc)Vector_mul,           /* nb_multiply */
    0,                                 /* nb_remainder */
    0,                                 /* nb_divmod */
    0,                                 /* nb_power */
    0,                                 /* nb_negative */
    0,                                 /* nb_positive */
    (unaryfunc)Vector_abs,            /* nb_absolute */
    (inquiry)Vector_bool,             /* nb_bool */
    0,                                 /* nb_invert */
    0,                                 /* nb_lshift */
    0,                                 /* nb_rshift */
    0,                                 /* nb_and */
    0,                                 /* nb_xor */
    0,                                 /* nb_or */
    0,                                 /* nb_int */
    0,                                 /* nb_reserved */
    0,                                 /* nb_float */
    0,                                 /* nb_inplace_add */
    0,                                 /* nb_inplace_subtract */
    0,                                 /* nb_inplace_multiply */
    0,                                 /* nb_inplace_remainder */
    0,                                 /* nb_inplace_power */
    0,                                 /* nb_inplace_lshift */
    0,                                 /* nb_inplace_rshift */
    0,                                 /* nb_inplace_and */
    0,                                 /* nb_inplace_xor */
    0,                                 /* nb_inplace_or */
    0,                                 /* nb_floor_divide */
    (binaryfunc)Vector_truediv,       /* nb_true_divide */
    0,                                 /* nb_inplace_floor_divide */
    0,                                 /* nb_inplace_true_divide */
    0,                                 /* nb_index */
    (binaryfunc)Vector_matmul,        /* nb_matrix_multiply */
    0,                                 /* nb_inplace_matrix_multiply */
};

/* Type definition */
static PyTypeObject VectorType = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "matmath._vector.Vector",
    .tp_doc = "Vector objects",
    .tp_basicsize = sizeof(VectorObject),
    .tp_itemsize = 0,
    .tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,
    .tp_new = Vector_new,
    .tp_init = (initproc)Vector_init,
    .tp_dealloc = (destructor)Vector_dealloc,
    .tp_repr = (reprfunc)Vector_repr,
    .tp_str = (reprfunc)Vector_str,
    .tp_as_number = &Vector_as_number,
    .tp_as_sequence = &Vector_as_sequence,
    .tp_hash = (hashfunc)Vector_hash,
    .tp_richcompare = (richcmpfunc)Vector_richcompare,
    .tp_methods = Vector_methods,
};

/* Module definition */
static PyModuleDef vectormodule = {
    PyModuleDef_HEAD_INIT,
    .m_name = "_vector",
    .m_doc = "C extension for Vector class",
    .m_size = -1,
};

/* Module initialization */
PyMODINIT_FUNC PyInit__vector(void) {
    PyObject *m;
    if (PyType_Ready(&VectorType) < 0)
        return NULL;

    m = PyModule_Create(&vectormodule);
    if (m == NULL)
        return NULL;

    Py_INCREF(&VectorType);
    if (PyModule_AddObject(m, "Vector", (PyObject *)&VectorType) < 0) {
        Py_DECREF(&VectorType);
        Py_DECREF(m);
        return NULL;
    }

    return m;
}
