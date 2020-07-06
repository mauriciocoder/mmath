import pytest
import math
# import nose.tools as nt  # contains testing tools like ok_, eq_, etc.
import mmath.statistics as st

def assertList():
    with pytest.raises(ValueError):
        st.mean([])
        st.mean(None)
        st.mean(10)
        st.mean("a")

def test_mean():
    assertList()
    assert st.mean([1, 2, 3]) == 2
    assert st.mean([1, 1, 2, 3, 3]) == 2
    assert st.mean([10, 100]) == 55
    assert st.mean([1, 1.5, 2]) == 1.5

def test_mad():
    assertList()
    assert st.mad([3, 8, 10, 17, 24, 27]) == 7.833333333333332

def test_median():
    assertList()
    assert st.median([1, 2, 3]) == 2
    assert st.median([1, 2, 3, 4]) == 2.5

def test_range():
    assertList()
    assert st.range([1, 2, 3]) == 2
    assert st.range([1, 2, 3, 4]) == 3

def test_quarter():
    assertList()
    # extremes and median for odds
    assert st.quarter([1, 2, 3], 0) == 1
    assert st.quarter([1, 2, 3], 2) == 2
    assert st.quarter([1, 2, 3], 4) == 3
    # extremes and median for evens
    assert st.quarter([1, 2, 3, 4], 0) == 1
    assert st.quarter([1, 2, 3, 4], 2) == 2.5
    assert st.quarter([1, 2, 3, 4], 4) == 4
    # first quartile for odds
    assert st.quarter([1, 2, 3], 1) == 1.5
    # first quartile for evens
    assert st.quarter([1, 2, 3, 4], 1) == 1.5
    # third quartile for odds
    assert st.quarter([1, 2, 3], 3) == 2.5
    # third quartile for evens
    assert st.quarter([1, 2, 3, 4], 3) == 3.5
    # single item test
    assert st.quarter([1], 0) == 1
    assert st.quarter([1], 1) == 1
    assert st.quarter([1], 2) == 1
    assert st.quarter([1], 3) == 1
    assert st.quarter([1], 4) == 1
    # two items test
    assert st.quarter([1, 2], 0) == 1
    assert st.quarter([1, 2], 1) == 1
    assert st.quarter([1, 2], 2) == 1.5
    assert st.quarter([1, 2], 3) == 2
    assert st.quarter([1, 2], 4) == 2

def test_iqr():
    assert st.iqr([1, 2, 3]) == 1
    assert st.iqr([1, 2, 3, 4]) == 2
    assert st.iqr([1, 2, 3, 4, 5]) == 2

def test_variance():
    values = [1, 2, 3, 4, 5, 6]
    assert st.variance(values, len(values)) == 2.9166666666666665

def test_variancePopulation():
    values = [1, 2, 3, 4, 5, 6]
    assert st.variancePopulation(values) == 2.9166666666666665

def test_varianceSample():
    values = [1, 2, 3, 4, 5, 6]
    assert st.varianceSample(values) == 3.5

def test_standardDev():
    values = [1, 2, 3, 4, 5, 6]
    assert st.standardDev(values, len(values)) == math.sqrt(2.9166666666666665)

def test_standardDevPopulation():
    values = [1, 2, 3, 4, 5, 6]
    assert st.standardDevPopulation(values) == math.sqrt(2.9166666666666665)

def test_standardDevSample():
    values = [1, 2, 3, 4, 5, 6]
    assert st.standardDevSample(values) == math.sqrt(3.5)

def test_zScore():
    assert st.zScore(60, 15, 70) == 0.6666666666666666
