import pytest

@pytest.mark.regression
@pytest.mark.parametrize("username,password",[("myuser1","mypass1"),("myuser2","mypass2"),("myuser3","mypass3")   ])
def test_assert_one(username,password):
    print("user:",username)
    print("password:", password)
