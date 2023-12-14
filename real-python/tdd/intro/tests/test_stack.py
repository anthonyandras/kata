from ds.stack import Stack
import pytest


@pytest.fixture
def stack():
    return Stack()


def test_constructor(stack):
    assert isinstance(stack, Stack)
    assert len(stack) == 0


def test_push(stack):
    stack.push(10)
    assert len(stack) == 1
    stack.push(5)
    assert len(stack) == 2


def test_pop(stack):
    stack.push(10)
    assert len(stack) == 1
    value = stack.pop()
    assert len(stack) == 0
    assert value == 10
