

# Implementation of what was in the handout on 2x2 matrix inversion is needed.

# The reason is that Newton's method in two dimensions involves inverting a
# 2x2 Hessian.


def invert_2x2(a, b, c, d):

    determinant = 1/(a*c-b*c)

    e = determinant * d
    f = determinant * -b
    g = determinant * -c
    h = determinant * a

    newtons_matrix = e,f,g,h

    return newtons_matrix