# mypy: disable-error-code="arg-type"

import pytest

from example1.covariance import (
    delegate_produce_a,
    delegate_produce_b,
    delegate_produce_c,
    delegate_produce_d,
)
from example1.world import (
    produce_a,
    produce_b,
    produce_c,
    produce_d,
)


def test_delegate_produce_a() -> None:
    delegate_produce_a(produce_a)

    delegate_produce_a(produce_b)

    delegate_produce_a(produce_c)

    delegate_produce_a(produce_d)


def test_delegate_produce_b() -> None:
    with pytest.raises(AttributeError, match="'A' object has no attribute 'print_b'"):
        delegate_produce_b(produce_a)

    delegate_produce_b(produce_b)

    delegate_produce_b(produce_c)

    with pytest.raises(AttributeError, match="'D' object has no attribute 'print_b'"):
        delegate_produce_b(produce_d)


def test_delegate_produce_c() -> None:
    with pytest.raises(AttributeError, match="'A' object has no attribute 'print_b'"):
        delegate_produce_c(produce_a)

    with pytest.raises(AttributeError, match="'B' object has no attribute 'print_c'"):
        delegate_produce_c(produce_b)

    delegate_produce_c(produce_c)

    with pytest.raises(AttributeError, match="'D' object has no attribute 'print_b'"):
        delegate_produce_c(produce_d)


def test_delegate_produce_d() -> None:
    with pytest.raises(AttributeError, match="'A' object has no attribute 'print_d'"):
        delegate_produce_d(produce_a)

    with pytest.raises(AttributeError, match="'B' object has no attribute 'print_d'"):
        delegate_produce_d(produce_b)

    with pytest.raises(AttributeError, match="'C' object has no attribute 'print_d'"):
        delegate_produce_d(produce_c)

    delegate_produce_d(produce_d)
