# importing necessary modules
import numpy as np
import matplotlib.pyplot as plt


class Differentiable:
    def __init__(self, value):  # initializing the object
        self._value = value

    def __call__(self):  # returning the value of the object
        return self._value

    def diff(self):
        x = self._value[0]  # splitting the array into x and y
        y = self._value[1]
        ydiff = [(y[i + 1] - y[i]) / (x[i + 1] - x[i]) for i in range(len(y) - 1)]  # calculating the derivative
        return type(self)(np.array([x[:-1], ydiff]))  # returning the derivative as a new object

    @classmethod
    def from_file(cls, path, delimiter=","):  # constructing an object from a file
        with open(path, 'r') as f:
            value = np.genfromtxt(f, delimiter=delimiter, unpack=True)
        return cls(value)


def main():
    data = Differentiable.from_file('data.csv')  # creating an object from the file
    plt.plot(*data())  # plotting the data
    plt.plot(*data.diff()())  # plotting the derivative
    plt.show()  # showing the plot


if __name__ == '__main__':
    main()  # calling the main function
