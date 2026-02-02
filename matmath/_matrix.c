#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <math.h>
#include <structmember.h>

/* Matrix object structure */
typedef struct {
    PyObject_HEAD
    double **data;
    Py_ssize_t rows;
    Py_ssize_t cols;
} MatrixObject;

/* Forward declarations */
static PyTypeObject MatrixType;

/* Helper function to allocate 2D array */
static double** alloc_matrix(Py_ssize_t rows, Py_ssize_t cols) {
    double **matrix = (double **)PyMem_Malloc(rows * sizeof(double *));
    if (matrix == NULL) {
        return NULL;
    }
    for (Py_ssize_t i = 0; i < rows; i++) {
        matrix[i] = (double *)PyMem_Malloc(cols * sizeof(double));
        if (matrix[i] == NULL) {
            for (Py_ssize_t j = 0; j < i; j++) {
                PyMem_Free(matrix[j]);
            }
            PyMem_Free(matrix);
            return NULL;
        }
    }
    return matrix;
}

/* Helper function to free 2D array */
static void free_matrix(double **matrix, Py_ssize_t rows) {
    if (matrix != NULL) {
        for (Py_ssize_t i = 0; i < rows; i++) {
            if (matrix[i] != NULL) {
                PyMem_Free(matrix[i]);
            }
        }
        PyMem_Free(matrix);
    }
}

/* Helper function to create a new Matrix */
static MatrixObject* Matrix_new_from_data(double **data, Py_ssize_t rows, Py_ssize_t cols) {
    MatrixObject *self = (MatrixObject *)MatrixType.tp_alloc(&MatrixType, 0);
    if (self != NULL) {
        self->data = alloc_matrix(rows, cols);
        if (self->data == NULL) {
            Py_DECREF(self);
            return (MatrixObject *)PyErr_NoMemory();
        }
        for (Py_ssize_t i = 0; i < rows; i++) {
            for (Py_ssize_t j = 0; j < cols; j++) {
                self->data[i][j] = data[i][j];
            }
        }
        self->rows = rows;
        self->cols = cols;
    }
    return self;
}

/* Matrix.__new__ */
static PyObject* Matrix_new(PyTypeObject *type, PyObject *args, PyObject *kwds) {
    MatrixObject *self;
    self = (MatrixObject *)type->tp_alloc(type, 0);
    if (self != NULL) {
        self->data = NULL;
        self->rows = 0;
        self->cols = 0;
    }
    return (PyObject *)self;
}

/* Matrix.__init__ */
static int Matrix_init(MatrixObject *self, PyObject *args, PyObject *kwds) {
    PyObject *mat;
    static char *kwlist[] = {"mat", NULL};

    if (!PyArg_ParseTupleAndKeywords(args, kwds, "O", kwlist, &mat)) {
        return -1;
    }

    if (!PyList_Check(mat)) {
        PyErr_SetString(PyExc_TypeError, "Argument must be a list of lists");
        return -1;
    }

    Py_ssize_t rows = PyList_Size(mat);
    if (rows == 0) {
        PyErr_SetString(PyExc_ValueError, "Matrix cannot be empty");
        return -1;
    }

    PyObject *first_row = PyList_GetItem(mat, 0);
    if (!PyList_Check(first_row)) {
        PyErr_SetString(PyExc_TypeError, "Matrix must be a list of lists");
        return -1;
    }

    Py_ssize_t cols = PyList_Size(first_row);
    if (cols == 0) {
        PyErr_SetString(PyExc_ValueError, "Matrix rows cannot be empty");
        return -1;
    }

    /* Allocate matrix */
    double **data = alloc_matrix(rows, cols);
    if (data == NULL) {
        PyErr_NoMemory();
        return -1;
    }

    /* Fill matrix and validate */
    for (Py_ssize_t i = 0; i < rows; i++) {
        PyObject *row = PyList_GetItem(mat, i);
        if (!PyList_Check(row)) {
            free_matrix(data, rows);
            PyErr_SetString(PyExc_TypeError, "All rows must be lists");
            return -1;
        }
        
        if (PyList_Size(row) != cols) {
            free_matrix(data, rows);
            PyErr_SetString(PyExc_ValueError, "The matrix is not a proper matrix.");
            return -1;
        }
        
        for (Py_ssize_t j = 0; j < cols; j++) {
            PyObject *item = PyList_GetItem(row, j);
            if (!PyFloat_Check(item) && !PyLong_Check(item)) {
                free_matrix(data, rows);
                PyErr_SetString(PyExc_TypeError, "All elements must be numbers");
                return -1;
            }
            data[i][j] = PyFloat_AsDouble(item);
        }
    }

    /* Free old data if exists */
    if (self->data != NULL) {
        free_matrix(self->data, self->rows);
    }

    self->data = data;
    self->rows = rows;
    self->cols = cols;
    return 0;
}

/* Matrix.__dealloc__ */
static void Matrix_dealloc(MatrixObject *self) {
    if (self->data != NULL) {
        free_matrix(self->data, self->rows);
    }
    Py_TYPE(self)->tp_free((PyObject *)self);
}

/* Matrix.__len__ */
static Py_ssize_t Matrix_length(MatrixObject *self) {
    return self->rows;
}

/* Matrix.__getitem__ */
static PyObject* Matrix_getitem(MatrixObject *self, Py_ssize_t index) {
    if (index < 0 || index >= self->rows) {
        PyErr_SetString(PyExc_IndexError, "Matrix row index out of range");
        return NULL;
    }
    
    PyObject *row = PyList_New(self->cols);
    if (row == NULL) {
        return NULL;
    }
    
    for (Py_ssize_t j = 0; j < self->cols; j++) {
        PyObject *item = PyFloat_FromDouble(self->data[index][j]);
        if (item == NULL) {
            Py_DECREF(row);
            return NULL;
        }
        PyList_SET_ITEM(row, j, item);
    }
    
    return row;
}

/* Matrix.__repr__ */
static PyObject* Matrix_repr(MatrixObject *self) {
    PyObject *result = PyUnicode_FromString("Matrix(");
    
    for (Py_ssize_t i = 0; i < self->rows; i++) {
        if (i > 0) {
            PyObject *temp = PyUnicode_Concat(result, PyUnicode_FromString(",\n       "));
            Py_DECREF(result);
            result = temp;
        }
        
        for (Py_ssize_t j = 0; j < self->cols; j++) {
            if (j > 0) {
                PyObject *temp = PyUnicode_Concat(result, PyUnicode_FromString(", "));
                Py_DECREF(result);
                result = temp;
            }
            PyObject *num = PyUnicode_FromFormat("%.10g", self->data[i][j]);
            PyObject *temp = PyUnicode_Concat(result, num);
            Py_DECREF(result);
            Py_DECREF(num);
            result = temp;
        }
    }
    
    PyObject *temp = PyUnicode_Concat(result, PyUnicode_FromString(")"));
    Py_DECREF(result);
    return temp;
}

/* Matrix.__str__ */
static PyObject* Matrix_str(MatrixObject *self) {
    /* Build column widths */
    Py_ssize_t *widths = (Py_ssize_t *)PyMem_Malloc(self->cols * sizeof(Py_ssize_t));
    if (widths == NULL) {
        return PyErr_NoMemory();
    }
    
    for (Py_ssize_t j = 0; j < self->cols; j++) {
        widths[j] = 0;
        for (Py_ssize_t i = 0; i < self->rows; i++) {
            char buffer[64];
            snprintf(buffer, sizeof(buffer), "%.10g", self->data[i][j]);
            Py_ssize_t len = strlen(buffer);
            if (len > widths[j]) {
                widths[j] = len;
            }
        }
    }
    
    /* Build string */
    PyObject *result = PyUnicode_FromString("");
    for (Py_ssize_t i = 0; i < self->rows; i++) {
        if (i > 0) {
            PyObject *temp = PyUnicode_Concat(result, PyUnicode_FromString("|\n"));
            Py_DECREF(result);
            result = temp;
        }
        
        PyObject *temp = PyUnicode_Concat(result, PyUnicode_FromString("| "));
        Py_DECREF(result);
        result = temp;
        
        for (Py_ssize_t j = 0; j < self->cols; j++) {
            char buffer[128];
            snprintf(buffer, sizeof(buffer), "%*.10g ", (int)widths[j], self->data[i][j]);
            temp = PyUnicode_Concat(result, PyUnicode_FromString(buffer));
            Py_DECREF(result);
            result = temp;
        }
    }
    
    PyObject *temp = PyUnicode_Concat(result, PyUnicode_FromString("|"));
    Py_DECREF(result);
    PyMem_Free(widths);
    return temp;
}

/* Matrix.__add__ */
static PyObject* Matrix_add(MatrixObject *self, PyObject *other) {
    if (!PyObject_TypeCheck(other, &MatrixType)) {
        PyErr_SetString(PyExc_TypeError, "Can only add Matrix to Matrix");
        return NULL;
    }
    
    MatrixObject *other_mat = (MatrixObject *)other;
    if (self->rows != other_mat->rows || self->cols != other_mat->cols) {
        PyErr_SetString(PyExc_ValueError, "The 2 matrices do not have the same order.");
        return NULL;
    }
    
    double **result_data = alloc_matrix(self->rows, self->cols);
    if (result_data == NULL) {
        return PyErr_NoMemory();
    }
    
    for (Py_ssize_t i = 0; i < self->rows; i++) {
        for (Py_ssize_t j = 0; j < self->cols; j++) {
            result_data[i][j] = self->data[i][j] + other_mat->data[i][j];
        }
    }
    
    MatrixObject *result = Matrix_new_from_data(result_data, self->rows, self->cols);
    free_matrix(result_data, self->rows);
    return (PyObject *)result;
}

/* Matrix.__sub__ */
static PyObject* Matrix_sub(MatrixObject *self, PyObject *other) {
    if (!PyObject_TypeCheck(other, &MatrixType)) {
        PyErr_SetString(PyExc_TypeError, "Can only subtract Matrix from Matrix");
        return NULL;
    }
    
    MatrixObject *other_mat = (MatrixObject *)other;
    if (self->rows != other_mat->rows || self->cols != other_mat->cols) {
        PyErr_SetString(PyExc_ValueError, "The 2 matrices do not have the same order.");
        return NULL;
    }
    
    double **result_data = alloc_matrix(self->rows, self->cols);
    if (result_data == NULL) {
        return PyErr_NoMemory();
    }
    
    for (Py_ssize_t i = 0; i < self->rows; i++) {
        for (Py_ssize_t j = 0; j < self->cols; j++) {
            result_data[i][j] = self->data[i][j] - other_mat->data[i][j];
        }
    }
    
    MatrixObject *result = Matrix_new_from_data(result_data, self->rows, self->cols);
    free_matrix(result_data, self->rows);
    return (PyObject *)result;
}

/* Matrix.__mul__ */
static PyObject* Matrix_mul(MatrixObject *self, PyObject *other) {
    double **result_data = alloc_matrix(self->rows, self->cols);
    if (result_data == NULL) {
        return PyErr_NoMemory();
    }
    
    if (PyFloat_Check(other) || PyLong_Check(other)) {
        /* Scalar multiplication */
        double scalar = PyFloat_AsDouble(other);
        for (Py_ssize_t i = 0; i < self->rows; i++) {
            for (Py_ssize_t j = 0; j < self->cols; j++) {
                result_data[i][j] = self->data[i][j] * scalar;
            }
        }
    } else if (PyObject_TypeCheck(other, &MatrixType)) {
        /* Element-wise multiplication */
        MatrixObject *other_mat = (MatrixObject *)other;
        if (self->rows != other_mat->rows || self->cols != other_mat->cols) {
            free_matrix(result_data, self->rows);
            PyErr_SetString(PyExc_ValueError, "The 2 matrices do not have the same order.");
            return NULL;
        }
        for (Py_ssize_t i = 0; i < self->rows; i++) {
            for (Py_ssize_t j = 0; j < self->cols; j++) {
                result_data[i][j] = self->data[i][j] * other_mat->data[i][j];
            }
        }
    } else {
        free_matrix(result_data, self->rows);
        PyErr_SetString(PyExc_TypeError, "Multiplication not supported between Matrix and given type.");
        return NULL;
    }
    
    MatrixObject *result = Matrix_new_from_data(result_data, self->rows, self->cols);
    free_matrix(result_data, self->rows);
    return (PyObject *)result;
}

/* Matrix.__matmul__ (matrix multiplication) */
static PyObject* Matrix_matmul(MatrixObject *self, PyObject *other) {
    if (!PyObject_TypeCheck(other, &MatrixType)) {
        PyErr_SetString(PyExc_TypeError, "Can only matrix multiply Matrix with Matrix");
        return NULL;
    }
    
    MatrixObject *other_mat = (MatrixObject *)other;
    if (self->cols != other_mat->rows) {
        PyErr_SetString(PyExc_ValueError, "Matrix dimensions incompatible for multiplication");
        return NULL;
    }
    
    double **result_data = alloc_matrix(self->rows, other_mat->cols);
    if (result_data == NULL) {
        return PyErr_NoMemory();
    }
    
    /* Initialize to zero */
    for (Py_ssize_t i = 0; i < self->rows; i++) {
        for (Py_ssize_t j = 0; j < other_mat->cols; j++) {
            result_data[i][j] = 0.0;
        }
    }
    
    /* Matrix multiplication */
    for (Py_ssize_t i = 0; i < self->rows; i++) {
        for (Py_ssize_t j = 0; j < other_mat->cols; j++) {
            for (Py_ssize_t k = 0; k < self->cols; k++) {
                result_data[i][j] += self->data[i][k] * other_mat->data[k][j];
            }
        }
    }
    
    MatrixObject *result = Matrix_new_from_data(result_data, self->rows, other_mat->cols);
    free_matrix(result_data, self->rows);
    return (PyObject *)result;
}

/* Matrix.__truediv__ */
static PyObject* Matrix_truediv(MatrixObject *self, PyObject *other) {
    double **result_data = alloc_matrix(self->rows, self->cols);
    if (result_data == NULL) {
        return PyErr_NoMemory();
    }
    
    if (PyFloat_Check(other) || PyLong_Check(other)) {
        /* Scalar division */
        double scalar = PyFloat_AsDouble(other);
        if (scalar == 0.0) {
            free_matrix(result_data, self->rows);
            PyErr_SetString(PyExc_ZeroDivisionError, "Division by zero");
            return NULL;
        }
        for (Py_ssize_t i = 0; i < self->rows; i++) {
            for (Py_ssize_t j = 0; j < self->cols; j++) {
                result_data[i][j] = self->data[i][j] / scalar;
            }
        }
    } else if (PyObject_TypeCheck(other, &MatrixType)) {
        /* Element-wise division */
        MatrixObject *other_mat = (MatrixObject *)other;
        if (self->rows != other_mat->rows || self->cols != other_mat->cols) {
            free_matrix(result_data, self->rows);
            PyErr_SetString(PyExc_ValueError, "The 2 matrices do not have the same order.");
            return NULL;
        }
        for (Py_ssize_t i = 0; i < self->rows; i++) {
            for (Py_ssize_t j = 0; j < self->cols; j++) {
                if (other_mat->data[i][j] == 0.0) {
                    free_matrix(result_data, self->rows);
                    PyErr_SetString(PyExc_ZeroDivisionError, "Division by zero");
                    return NULL;
                }
                result_data[i][j] = self->data[i][j] / other_mat->data[i][j];
            }
        }
    } else {
        free_matrix(result_data, self->rows);
        PyErr_SetString(PyExc_TypeError, "Division not supported between Matrix and given type.");
        return NULL;
    }
    
    MatrixObject *result = Matrix_new_from_data(result_data, self->rows, self->cols);
    free_matrix(result_data, self->rows);
    return (PyObject *)result;
}

/* Matrix.transpose */
static PyObject* Matrix_transpose(MatrixObject *self, PyObject *Py_UNUSED(ignored)) {
    double **result_data = alloc_matrix(self->cols, self->rows);
    if (result_data == NULL) {
        return PyErr_NoMemory();
    }
    
    for (Py_ssize_t i = 0; i < self->cols; i++) {
        for (Py_ssize_t j = 0; j < self->rows; j++) {
            result_data[i][j] = self->data[j][i];
        }
    }
    
    MatrixObject *result = Matrix_new_from_data(result_data, self->cols, self->rows);
    free_matrix(result_data, self->cols);
    return (PyObject *)result;
}

/* Matrix.determinant */
static PyObject* Matrix_determinant(MatrixObject *self, PyObject *Py_UNUSED(ignored)) {
    if (self->rows != self->cols) {
        PyErr_SetString(PyExc_ValueError, "The given matrix is not a square matrix.");
        return NULL;
    }
    
    /* Create a copy for Gaussian elimination */
    double **mat = alloc_matrix(self->rows, self->cols);
    if (mat == NULL) {
        return PyErr_NoMemory();
    }
    
    for (Py_ssize_t i = 0; i < self->rows; i++) {
        for (Py_ssize_t j = 0; j < self->cols; j++) {
            mat[i][j] = self->data[i][j];
        }
    }
    
    double determinant = 1.0;
    
    for (Py_ssize_t i = 0; i < self->rows; i++) {
        for (Py_ssize_t j = i + 1; j < self->rows; j++) {
            if (mat[i][i] == 0.0) {
                mat[i][i] = 1.0;
            }
            double x = mat[j][i] / mat[i][i];
            for (Py_ssize_t k = 0; k < self->rows; k++) {
                mat[j][k] -= x * mat[i][k];
            }
        }
    }
    
    for (Py_ssize_t i = 0; i < self->rows; i++) {
        determinant *= mat[i][i];
    }
    
    free_matrix(mat, self->rows);
    return PyFloat_FromDouble(determinant);
}

/* Matrix.trace */
static PyObject* Matrix_trace(MatrixObject *self, PyObject *Py_UNUSED(ignored)) {
    if (self->rows != self->cols) {
        PyErr_SetString(PyExc_ValueError, "The given matrix is not a square matrix.");
        return NULL;
    }
    
    double total = 0.0;
    for (Py_ssize_t i = 0; i < self->rows; i++) {
        total += self->data[i][i];
    }
    
    return PyFloat_FromDouble(total);
}

/* Matrix.is_square */
static PyObject* Matrix_is_square(MatrixObject *self, PyObject *Py_UNUSED(ignored)) {
    if (self->rows == self->cols) {
        Py_RETURN_TRUE;
    }
    Py_RETURN_FALSE;
}

/* Matrix.is_symmetric */
static PyObject* Matrix_is_symmetric(MatrixObject *self, PyObject *Py_UNUSED(ignored)) {
    if (self->rows != self->cols) {
        Py_RETURN_FALSE;
    }
    
    for (Py_ssize_t i = 0; i < self->rows; i++) {
        for (Py_ssize_t j = i; j < self->cols; j++) {
            if (self->data[i][j] != self->data[j][i]) {
                Py_RETURN_FALSE;
            }
        }
    }
    Py_RETURN_TRUE;
}

/* Matrix.is_diagonal */
static PyObject* Matrix_is_diagonal(MatrixObject *self, PyObject *Py_UNUSED(ignored)) {
    if (self->rows != self->cols) {
        Py_RETURN_FALSE;
    }
    
    for (Py_ssize_t i = 0; i < self->rows; i++) {
        for (Py_ssize_t j = 0; j < self->cols; j++) {
            if (i != j && self->data[i][j] != 0.0) {
                Py_RETURN_FALSE;
            }
        }
    }
    Py_RETURN_TRUE;
}

/* Matrix.is_identity */
static PyObject* Matrix_is_identity(MatrixObject *self, PyObject *Py_UNUSED(ignored)) {
    if (self->rows != self->cols) {
        Py_RETURN_FALSE;
    }
    
    for (Py_ssize_t i = 0; i < self->rows; i++) {
        for (Py_ssize_t j = 0; j < self->cols; j++) {
            double expected = (i == j) ? 1.0 : 0.0;
            if (fabs(self->data[i][j] - expected) > 1e-10) {
                Py_RETURN_FALSE;
            }
        }
    }
    Py_RETURN_TRUE;
}

/* Matrix.copy */
static PyObject* Matrix_copy(MatrixObject *self, PyObject *Py_UNUSED(ignored)) {
    return (PyObject *)Matrix_new_from_data(self->data, self->rows, self->cols);
}

/* Matrix.to_list */
static PyObject* Matrix_to_list(MatrixObject *self, PyObject *Py_UNUSED(ignored)) {
    PyObject *result = PyList_New(self->rows);
    if (result == NULL) {
        return NULL;
    }
    
    for (Py_ssize_t i = 0; i < self->rows; i++) {
        PyObject *row = PyList_New(self->cols);
        if (row == NULL) {
            Py_DECREF(result);
            return NULL;
        }
        
        for (Py_ssize_t j = 0; j < self->cols; j++) {
            PyObject *item = PyFloat_FromDouble(self->data[i][j]);
            if (item == NULL) {
                Py_DECREF(row);
                Py_DECREF(result);
                return NULL;
            }
            PyList_SET_ITEM(row, j, item);
        }
        
        PyList_SET_ITEM(result, i, row);
    }
    
    return result;
}

/* Matrix.order property */
static PyObject* Matrix_get_order(MatrixObject *self, void *closure) {
    return Py_BuildValue("(nn)", self->rows, self->cols);
}

/* Matrix.__eq__ */
static PyObject* Matrix_richcompare(MatrixObject *self, PyObject *other, int op) {
    if (!PyObject_TypeCheck(other, &MatrixType)) {
        if (op == Py_EQ) {
            Py_RETURN_FALSE;
        } else if (op == Py_NE) {
            Py_RETURN_TRUE;
        }
        Py_RETURN_NOTIMPLEMENTED;
    }
    
    MatrixObject *other_mat = (MatrixObject *)other;
    
    if (op == Py_EQ) {
        if (self->rows != other_mat->rows || self->cols != other_mat->cols) {
            Py_RETURN_FALSE;
        }
        for (Py_ssize_t i = 0; i < self->rows; i++) {
            for (Py_ssize_t j = 0; j < self->cols; j++) {
                if (self->data[i][j] != other_mat->data[i][j]) {
                    Py_RETURN_FALSE;
                }
            }
        }
        Py_RETURN_TRUE;
    } else if (op == Py_NE) {
        if (self->rows != other_mat->rows || self->cols != other_mat->cols) {
            Py_RETURN_TRUE;
        }
        for (Py_ssize_t i = 0; i < self->rows; i++) {
            for (Py_ssize_t j = 0; j < self->cols; j++) {
                if (self->data[i][j] != other_mat->data[i][j]) {
                    Py_RETURN_TRUE;
                }
            }
        }
        Py_RETURN_FALSE;
    }
    
    Py_RETURN_NOTIMPLEMENTED;
}

/* Method definitions */
static PyMethodDef Matrix_methods[] = {
    {"transpose", (PyCFunction)Matrix_transpose, METH_NOARGS, "Transpose the matrix"},
    {"determinant", (PyCFunction)Matrix_determinant, METH_NOARGS, "Calculate determinant"},
    {"det", (PyCFunction)Matrix_determinant, METH_NOARGS, "Alias for determinant"},
    {"trace", (PyCFunction)Matrix_trace, METH_NOARGS, "Calculate trace"},
    {"is_square", (PyCFunction)Matrix_is_square, METH_NOARGS, "Check if square"},
    {"is_symmetric", (PyCFunction)Matrix_is_symmetric, METH_NOARGS, "Check if symmetric"},
    {"is_diagonal", (PyCFunction)Matrix_is_diagonal, METH_NOARGS, "Check if diagonal"},
    {"is_identity", (PyCFunction)Matrix_is_identity, METH_NOARGS, "Check if identity"},
    {"copy", (PyCFunction)Matrix_copy, METH_NOARGS, "Create a copy"},
    {"to_list", (PyCFunction)Matrix_to_list, METH_NOARGS, "Convert to list"},
    {NULL}
};

/* Property definitions */
static PyGetSetDef Matrix_getsetters[] = {
    {"order", (getter)Matrix_get_order, NULL, "Matrix order (rows, cols)", NULL},
    {"size", (getter)Matrix_get_order, NULL, "Alias for order", NULL},
    {NULL}
};

/* Sequence methods */
static PySequenceMethods Matrix_as_sequence = {
    (lenfunc)Matrix_length,           /* sq_length */
    0,                                 /* sq_concat */
    0,                                 /* sq_repeat */
    (ssizeargfunc)Matrix_getitem,     /* sq_item */
    0,                                 /* sq_slice */
    0,                                 /* sq_ass_item */
    0,                                 /* sq_ass_slice */
    0,                                 /* sq_contains */
};

/* Number methods */
static PyNumberMethods Matrix_as_number = {
    (binaryfunc)Matrix_add,           /* nb_add */
    (binaryfunc)Matrix_sub,           /* nb_subtract */
    (binaryfunc)Matrix_mul,           /* nb_multiply */
    0,                                 /* nb_remainder */
    0,                                 /* nb_divmod */
    0,                                 /* nb_power */
    0,                                 /* nb_negative */
    0,                                 /* nb_positive */
    0,                                 /* nb_absolute */
    0,                                 /* nb_bool */
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
    (binaryfunc)Matrix_truediv,       /* nb_true_divide */
    0,                                 /* nb_inplace_floor_divide */
    0,                                 /* nb_inplace_true_divide */
    0,                                 /* nb_index */
    (binaryfunc)Matrix_matmul,        /* nb_matrix_multiply */
    0,                                 /* nb_inplace_matrix_multiply */
};

/* Type definition */
static PyTypeObject MatrixType = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "matmath._matrix.Matrix",
    .tp_doc = "Matrix objects",
    .tp_basicsize = sizeof(MatrixObject),
    .tp_itemsize = 0,
    .tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,
    .tp_new = Matrix_new,
    .tp_init = (initproc)Matrix_init,
    .tp_dealloc = (destructor)Matrix_dealloc,
    .tp_repr = (reprfunc)Matrix_repr,
    .tp_str = (reprfunc)Matrix_str,
    .tp_as_number = &Matrix_as_number,
    .tp_as_sequence = &Matrix_as_sequence,
    .tp_richcompare = (richcmpfunc)Matrix_richcompare,
    .tp_methods = Matrix_methods,
    .tp_getset = Matrix_getsetters,
};

/* Module definition */
static PyModuleDef matrixmodule = {
    PyModuleDef_HEAD_INIT,
    .m_name = "_matrix",
    .m_doc = "C extension for Matrix class",
    .m_size = -1,
};

/* Module initialization */
PyMODINIT_FUNC PyInit__matrix(void) {
    PyObject *m;
    if (PyType_Ready(&MatrixType) < 0)
        return NULL;

    m = PyModule_Create(&matrixmodule);
    if (m == NULL)
        return NULL;

    Py_INCREF(&MatrixType);
    if (PyModule_AddObject(m, "Matrix", (PyObject *)&MatrixType) < 0) {
        Py_DECREF(&MatrixType);
        Py_DECREF(m);
        return NULL;
    }

    return m;
}
