import numpy as np  # importing necessary libraries
import matplotlib.pyplot as plt


AMOGUS = np.array([
        [0, 1, 1, 1],
        [1, 1, 0, 0],
        [1, 1, 1, 1],
        [0, 1, 0, 1]
    ])


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


class ParseFlights:
    def __init__(self, path, delimiter=";"):
        self._path = path
        self._delimiter = delimiter
        with open(path, 'r') as f:
            self._data = np.genfromtxt(f, delimiter=delimiter, unpack=True, dtype=str)
        self._data = self._data[1:]
        self._data = self._quadrant_parse(np.array(self._data))
        self.data = self._data

    def split(self):
        return np.array([self._data[0][0::4], self._data[1][0::4]]),\
               np.array([self._data[0][1::4], self._data[1][1::4]]),\
               np.array([self._data[0][2::4], self._data[1][2::4]]),\
               np.array([self._data[0][3::4], self._data[1][3::4]])

    @staticmethod
    @np.vectorize
    def _quadrant_parse(string):
        return float(string.replace("K1", ".0").replace("K2", ".25").replace("K3", ".50").replace("K4", ".75"))


def main():
    """
    data = Differentiable.from_file('data.csv')  # creating an object from the file
    plt.plot(*data())  # plotting the data
    plt.plot(*data.diff()())  # plotting the derivative
    plt.plot(*data.diff().diff()())  # plotting the second derivative
    plt.show()  # showing the plot
    """
    data = ParseFlights('08510_20220519-103541.csv')
    # K1, K2, K3, K4 = data.split()
    plt.plot(*data.data)
    plt.show()


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
