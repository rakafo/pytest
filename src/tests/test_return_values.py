import pytest

from src.return_values import return_val


def test_return_val(mocker):
  mock = mocker.patch('return_val')
  mock.return_value = mock
  mock.foo1 = 10
  assert return_val() == 10