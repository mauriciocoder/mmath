# -----------------------------------------------------------
# Custom statistical functions for Python
#
# (C) 2020 Maurico Bonetti
# Released under GNU Public License (GPL)
# email: mauricio.coder@outlook.com
# -----------------------------------------------------------
import math  
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
    u = mean(values)
    sum = reduce(lambda a, b: a + abs(b - u), values, 0)
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
    return values[-1] - values[0]

def quarter(values, index):
    """
    Calculates the quarter based on the following rule
    index = 0 -> returns the minimum value
    index = 1 -> returns the first quarter value
    index = 2 -> returns the median value
    index = 3 -> returns the third quarter value
    index = 4 -> returns the fourth quarter value
    """
    assertList(values)
    values.sort()
    if (index == 0):
        return values[0]
    if (index == 1):
        if (len(values) % 2 == 0):
            return median(values[0: len(values) // 2])
        else:
            return median(values[0: (len(values) // 2) + 1])
    if (index == 2):
        return median(values)
    if (index == 3):
        return median(values[len(values) // 2:])
    if (index == 4):
        return values[-1]

def iqr(values):
    """Calculates the IQR from values"""
    assertList(values)
    values.sort()
    return quarter(values, 3) - quarter(values, 1)

def variance(values, n):
    """Calculates the variance based on the sample and the population quantity n"""
    assertList(values)
    if (len(values) <= 1):
        return values[0]
    u = mean(values)
    sum = reduce(lambda a, b: a + abs(b - u) ** 2, values, 0)
    return sum / n

def variancePopulation(values):
    """Calculates the variance based on the whole population quantity (n)"""
    return variance(values, len(values))

def varianceSample(values):
    """Calculates the variance based on the sample quantity (n - 1)"""
    return variance(values, len(values) - 1)

def standardDev(values, n):
    """Calculates the standard deviation on the sample and the population quantity n"""
    return math.sqrt(variance(values, n))

def standardDevPopulation(values):
    """Calculates the standard deviation on the whole population quantity (n)"""
    return math.sqrt(variance(values, len(values)))

def standardDevSample(values):
    """Calculates the standard deviation on the sample and the population quantity n"""
    return math.sqrt(variance(values, len(values) - 1))

def zScore(mean, sDev, value):
    """Calculates the z-score(standard deviation times that a value is from the mean)"""
    return (value - mean) / sDev
