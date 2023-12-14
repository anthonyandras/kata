import pytest
from intro.ds.palidrome import is_palindrome


@pytest.mark.smoke
@pytest.mark.parametrize("palindrome", [
    "",
    "a",
    "Bob",
    "Never odd or even"
])
def test_palindrome(palindrome):
    assert is_palindrome(palindrome)


@pytest.mark.smoke
@pytest.mark.parametrize("palidrome", [
    "abc",
    "abab"
])
def test_not_palindrome(palidrome):
    assert not is_palindrome(palidrome)
