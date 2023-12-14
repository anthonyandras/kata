from intro.ds.stack import Stack
import pytest


@pytest.fixture
def stack():
    return Stack()


@pytest.mark.smoke
def test_constructor(stack):
    assert isinstance(stack, Stack)
    assert len(stack) == 0


@pytest.mark.smoke
# @pytest.mark.skip
def test_push(stack):
    stack.push(10)
    assert len(stack) == 1
    stack.push(5)
    assert len(stack) == 2


def test_pop(stack):
    stack.push("Hello")
    stack.push("World")
    assert len(stack) == 2
    assert stack.pop() == "World"
    assert stack.pop() == "Hello"
    assert stack.pop() is None
