# mypy: disable-error-code="arg-type"

import pytest

from example1.contravariance import (
    delegate_consume_a,
    delegate_consume_b,
    delegate_consume_c,
    delegate_consume_d,
)
from example1.world import (
    consume_a,
    consume_b,
    consume_c,
    consume_d,
)


def test_delegate_consume_a() -> None:
    delegate_consume_a(consume_a)

    with pytest.raises(AttributeError, match="'A' object has no attribute 'print_b'"):
        delegate_consume_a(consume_b)

    with pytest.raises(AttributeError, match="'A' object has no attribute 'print_b'"):
        delegate_consume_a(consume_c)

    with pytest.raises(AttributeError, match="'A' object has no attribute 'print_d'"):
        delegate_consume_a(consume_d)


def test_delegate_consume_b() -> None:
    delegate_consume_b(consume_a)

    delegate_consume_b(consume_b)

    with pytest.raises(AttributeError, match="'B' object has no attribute 'print_c'"):
        delegate_consume_b(consume_c)

    with pytest.raises(AttributeError, match="'B' object has no attribute 'print_d'"):
        delegate_consume_b(consume_d)


def test_delegate_consume_c() -> None:
    delegate_consume_c(consume_a)

    delegate_consume_c(consume_b)

    delegate_consume_c(consume_c)

    with pytest.raises(AttributeError, match="'C' object has no attribute 'print_d'"):
        delegate_consume_c(consume_d)


def test_delegate_consume_d() -> None:
    delegate_consume_d(consume_a)

    with pytest.raises(AttributeError, match="'D' object has no attribute 'print_b'"):
        delegate_consume_d(consume_b)

    with pytest.raises(AttributeError, match="'D' object has no attribute 'print_b'"):
        delegate_consume_d(consume_c)

    delegate_consume_d(consume_d)
