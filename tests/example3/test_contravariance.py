import pytest

from example3.contravariance import ConcreteASink, ConcreteBSink, with_a_sink, with_b_sink


def test_with_a_sink() -> None:
    with_a_sink(ConcreteASink())
    with pytest.raises(AttributeError, match="'A' object has no attribute 'do_b'"):
        with_a_sink(ConcreteBSink())


def test_with_b_sink() -> None:
    with_b_sink(ConcreteASink())
    with_b_sink(ConcreteBSink())
