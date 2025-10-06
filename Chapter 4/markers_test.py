import pytest


@pytest.mark.smoke
def test_assert_one():
    print("a<b")
    a=10
    b=20
    assert a<b

@pytest.mark.smoke
@pytest.mark.sanity
def test_assert_two():
    print("a>b")
    a=20
    b=10
    assert a>b

@pytest.mark.regression
def test_assert_three():
    print("a=b")
    a=20
    b=20
    assert a.__eq__(b)

@pytest.mark.regression
def test_assert_four():
    print("fail")
    a=20
    b=10
    assert a.__eq__(b),"A is not equal to B"


# @pytest.mark.regression (mark test as regression)
# @pytest.mark.smoke (mark test as smoke)
# pytest -rA -m regression(execute only regression)
# pytest -rA -m sanity(execute only sanity)
# pytest -rA -m regression(execute only regression)