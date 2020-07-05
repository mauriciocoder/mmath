import pytest
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

    
