# -----------------------------------------------------------
# Custom statistical functions for Python
#
# (C) 2020 Maurico Bonetti
# Released under GNU Public License (GPL)
# email: mauricio.coder@outlook.com
# -----------------------------------------------------------
# TODO: iqr/ variance/ standard deviation
from functools import reduce

def assertList(values):
    if not values:
        raise ValueError

def mean(values):
    """Calculates the mean value from values list"""
    assertList(values)
    sum = reduce(lambda a, b: a + b, values)
    return sum / len(values)

def mad(values):
    """Calculates the mad(mean absolute distribution) value from values list"""
    assertList(values)
    meanValue = mean(values)
    sum = reduce(lambda a, b: a + abs(b - meanValue), values, 0)
    return sum / len(values)

def median(values):
    """Calculates the median value from values list"""
    assertList(values)
    values.sort()
    valuesLen = len(values)
    if (valuesLen % 2 == 0):
        i = valuesLen // 2
        return (values[i - 1] + values[i]) / 2
    else:
        return values[valuesLen // 2]

def range(values):
    """Calculates the range from values list"""
    assertList(values)
    values.sort()
    return values[len(values) - 1] - values[0]
