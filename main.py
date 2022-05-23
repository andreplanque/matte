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
    plt.plot(*data.diff().diff()())  # plotting the second derivative
    plt.show()  # showing the plot


if __name__ == '__main__':
    main()  # calling the main function

    # Did you ever hear the tragedy of Darth Plagueis The Wise? I thought not. It's not
    # a story the Jedi would tell you. It's a Sith legend. Darth Plagueis was a Dark
    # Lord of the Sith, so powerful and so wise he could use the Force to influence the
    # midichlorians to create life... He had such a knowledge of the dark side that he
    # could even keep the ones he cared about from dying. The dark side of the Force is a
    # pathway to many abilities some consider to be unnatural. He became so powerful...
    # The only thing he was afraid of was losing his power, which eventually, of course,
    # he did. Unfortunately, he taught his apprentice everything he knew, then his
    # apprentice killed him in his sleep. Ironic. He could save others from death, but
    # not himself.
