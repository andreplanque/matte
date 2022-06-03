import matplotlib.pyplot as plt
import numpy as np  # importing necessary libraries


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


class ParseFlights:
    def __init__(self, path, delimiter=";"):  # initializing the object
        with open(path, 'r') as f:
            self._data = np.genfromtxt(f, delimiter=delimiter, unpack=True, dtype=str)
        self._data = self._data[1:]  # removing the first row
        self._data = self._quadrant_parse(np.array(self._data))  # turning the string into a fraction

    def __call__(self):  # returning the data
        return self._data

    def split(self):  # splitting the data into the four quadrants
        return Differentiable(np.array([self._data[0][0::4], self._data[1][0::4]])),\
               Differentiable(np.array([self._data[0][1::4], self._data[1][1::4]])),\
               Differentiable(np.array([self._data[0][2::4], self._data[1][2::4]])),\
               Differentiable(np.array([self._data[0][3::4], self._data[1][3::4]]))

    @staticmethod
    @np.vectorize
    def _quadrant_parse(string):  # turning the string of K's into fractions
        return float(string.replace("K1", ".0").replace("K2", ".25").replace("K3", ".50").replace("K4", ".75"))


def main():
    flights = ParseFlights("08510_20220519-103541.csv")
    x, y, z, w = flights.split()  # splitting the data into four different quadrants
    x_growth = np.average(x.diff()()[1])  # finding the average growth rate of the quadrants
    y_growth = np.average(y.diff()()[1])
    z_growth = np.average(z.diff()()[1])
    w_growth = np.average(w.diff()()[1])
    time = list(flights()[0])  # getting the time data
    passengers = list(flights()[1])  # getting the passenger data

    for _ in range(3):
        time += [time[-4] + 1,
                 time[-3] + 1,
                 time[-2] + 1,
                 time[-1] + 1]  # adding the new time data
        passengers += [passengers[-4] + x_growth,
                       passengers[-3] + y_growth,
                       passengers[-2] + z_growth,
                       passengers[-1] + w_growth]  # adding the new predicted passenger data


AMOGUS = np.array([
        [0, 1, 1, 1],
        [1, 1, 0, 0],
        [1, 1, 1, 1],
        [0, 1, 0, 1]
    ])


if __name__ == '__main__':
    main()  # calling the main function
    plt.imshow(AMOGUS, cmap='gray_r')
    plt.show()


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

