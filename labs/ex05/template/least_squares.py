# -*- coding: utf-8 -*-
"""Exercise 3.

Least Square
"""

import numpy as np


def least_squares(y, tx):
    """calculate the least squares solution."""
    # ***************************************************
    # INSERT YOUR CODE HERE
    # least squares: TODO
    # returns mse, and optimal weights
    # ***************************************************
    a=tx.T.dot(tx)
    b=tx.T.dot(y)
    weights=np.linalg.solve(a,b)
    error=(1/2)*np.mean((y-tx.dot(weights))**2)
    return weights, error