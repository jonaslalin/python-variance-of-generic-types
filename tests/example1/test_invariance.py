# mypy: disable-error-code="arg-type"

import pytest

from example1.invariance import (
    delegate_consume_a_and_produce_a,
    delegate_consume_b_and_produce_b,
    delegate_consume_c_and_produce_c,
    delegate_consume_d_and_produce_d,
)
from example1.world import (
    consume_a_and_produce_a,
    consume_b_and_produce_b,
    consume_c_and_produce_c,
    consume_d_and_produce_d,
)


def test_delegate_consume_a_and_produce_a() -> None:
    delegate_consume_a_and_produce_a(consume_a_and_produce_a)

    with pytest.raises(AttributeError, match="'A' object has no attribute 'print_b'"):
        delegate_consume_a_and_produce_a(consume_b_and_produce_b)

    with pytest.raises(AttributeError, match="'A' object has no attribute 'print_b'"):
        delegate_consume_a_and_produce_a(consume_c_and_produce_c)

    with pytest.raises(AttributeError, match="'A' object has no attribute 'print_d'"):
        delegate_consume_a_and_produce_a(consume_d_and_produce_d)


def test_delegate_consume_b_and_produce_b() -> None:
    with pytest.raises(AttributeError, match="'A' object has no attribute 'print_b'"):
        delegate_consume_b_and_produce_b(consume_a_and_produce_a)

    delegate_consume_b_and_produce_b(consume_b_and_produce_b)

    with pytest.raises(AttributeError, match="'B' object has no attribute 'print_c'"):
        delegate_consume_b_and_produce_b(consume_c_and_produce_c)

    with pytest.raises(AttributeError, match="'B' object has no attribute 'print_d'"):
        delegate_consume_b_and_produce_b(consume_d_and_produce_d)


def test_delegate_consume_c_and_produce_c() -> None:
    with pytest.raises(AttributeError, match="'A' object has no attribute 'print_b'"):
        delegate_consume_c_and_produce_c(consume_a_and_produce_a)

    with pytest.raises(AttributeError, match="'B' object has no attribute 'print_c'"):
        delegate_consume_c_and_produce_c(consume_b_and_produce_b)

    delegate_consume_c_and_produce_c(consume_c_and_produce_c)

    with pytest.raises(AttributeError, match="'C' object has no attribute 'print_d'"):
        delegate_consume_c_and_produce_c(consume_d_and_produce_d)


def test_delegate_consume_d_and_produce_d() -> None:
    with pytest.raises(AttributeError, match="'A' object has no attribute 'print_d'"):
        delegate_consume_d_and_produce_d(consume_a_and_produce_a)

    with pytest.raises(AttributeError, match="'D' object has no attribute 'print_b'"):
        delegate_consume_d_and_produce_d(consume_b_and_produce_b)

    with pytest.raises(AttributeError, match="'D' object has no attribute 'print_b'"):
        delegate_consume_d_and_produce_d(consume_c_and_produce_c)

    delegate_consume_d_and_produce_d(consume_d_and_produce_d)
