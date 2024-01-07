import numpy as np
import sys

# import functions from PA #5.
from util import linear_regression, prepend_ones_column

def read_file(filename):
    '''
    Read data from the specified file.  Split the lines and convert
    float strings into floats.  Assumes the first row contains labels
    for the columns.

    Inputs:
      filename: name of the file to be read

    Returns:
      (list of strings, 2D array)
    '''
    with open(filename) as f:
        labels = f.readline().strip().split(',')
        data = np.loadtxt(f, delimiter=',', dtype=np.float64)
        return labels, data

def var(y):
    return ((y - y.mean()) ** 2).sum() / len(y)


def task2(b):
    ### Replace 0.0 with code to extract the desired slice
    print("rows 0, 1, and 2.")
    print(b[[0, 1, 2], :])
    print()
    print("rows 0, 1, and 5")
    print(b[[0, 1, 5], :])
    print()
    print("columns 0, 1, and 2")
    print(b[:, [0, 1, 2]])
    print()
    print("columns 0, 1, and 3")
    print(b[:, [0, 1, 3]])
    print()
    print("columns 0, 1, and 2 from rows 2 and 3.")
    print(b[2:4, [0, 1, 2]])
    print()

def go():
    city_col_names, city_data = read_file("city_data.csv")


    graffiti = city_data[:,0]
    garbage = city_data[:,3]



    print("Task 1")
    print("GRAFFITI:", var(graffiti))
    print("GARBAGE:", var(garbage))
    print()
    print()


    print("Task 2")
    b = (np.arange(24)**2).reshape(6,4)
    task2(b)


    print("Task 3")
    X = prepend_ones_column(city_data[:, [2,3]])
    y = city_data[:, 7]
    beta = linear_regression(X, y)
    print("Rodents, Garbage => Crime", beta)
    print()
    print()


    print("Task 4")
    X = prepend_ones_column(city_data[:, [0]])
    y = city_data[:, 7]
    beta = linear_regression(X, y)
    print("Graffiti => Crime:", beta)
    print()
    print()

if __name__ == "__main__":
    go()

