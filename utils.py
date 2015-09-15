import os
import numpy

__author__ = 'jambo'


PRACTICE_1_DIR = "/Users/jambo/Downloads/practice_1"


def load_csv(filepath):
    data = numpy.loadtxt(filepath, delimiter=",")
    return data[:, :-1], data[:, -1]


def load_prices(filepath=os.path.join(PRACTICE_1_DIR, "Linear_regression", "prices.txt")):
    return load_csv(filepath)

def load_chips(filepath=os.path.join(PRACTICE_1_DIR, "KNN", "chips.txt")):
    return load_csv(filepath)

def load_supermarket(filepath=os.path.join(PRACTICE_1_DIR, "Association_rules", "supermarket.arff")):
    pass

