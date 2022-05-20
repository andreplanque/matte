import numpy as np
import matplotlib.pyplot as plt


class Placeholder:
    def __init__(self, value):
        self._value = value

    def __call__(self):
        return self._value

    def diff(self):
        x = self._value[0]
        y = self._value[1]
        ydiff = [(y[i + 1] - y[i]) / (x[i + 1] - x[i]) for i in range(len(y) - 1)]
        return type(self)(np.array([x[:-1], ydiff]))

    @classmethod
    def from_file(cls, path, delimiter=","):
        with open(path, 'r') as f:
            value = np.genfromtxt(f, delimiter=delimiter, unpack=True)
        return cls(value)


def main():
    data = Placeholder.from_file('data.csv')
    plt.plot(*data())
    plt.plot(*data.diff()())
    plt.show()


if __name__ == '__main__':
    main()
