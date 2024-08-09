import pytest

from variance.contravariance import (
    ConcreteASink,
    ConcreteBSink,
    ConcreteCSink,
    with_some_a_sink,
    with_some_b_sink,
    with_some_c_sink,
)


def test_with_some_a_sink(capsys: pytest.CaptureFixture[str]) -> None:
    with_some_a_sink(ConcreteASink())
    captured_out = capsys.readouterr().out
    assert (
        captured_out
        == (
            "foo\n"  # from `a_sink.consume(a)`
            "foo\n"  # from `a_sink.consume(b)`
            "foo\n"  # from `a_sink.consume(c)`
        )
    )

    # with_some_a_sink(ConcreteBSink())

    # with_some_a_sink(ConcreteCSink())


def test_with_some_b_sink(capsys: pytest.CaptureFixture[str]) -> None:
    with_some_b_sink(ConcreteASink())
    captured_out = capsys.readouterr().out
    assert (
        captured_out
        == (
            "foo\n"  # from `a_sink.consume(b)`
            "foo\n"  # from `a_sink.consume(c)`
        )
    )

    with_some_b_sink(ConcreteBSink())
    captured_out = capsys.readouterr().out
    assert (
        captured_out
        == (
            "foo\n"  # from `b_sink.consume(b)`
            "bar\n"  # from `b_sink.consume(b)`
            "foo\n"  # from `b_sink.consume(c)`
            "bar\n"  # from `b_sink.consume(c)`
        )
    )

    # with_some_b_sink(ConcreteCSink())


def test_with_some_c_sink(capsys: pytest.CaptureFixture[str]) -> None:
    with_some_c_sink(ConcreteASink())
    captured_out = capsys.readouterr().out
    assert captured_out == (
        "foo\n"  # from `a_sink.consume(c)`
    )

    with_some_c_sink(ConcreteBSink())
    captured_out = capsys.readouterr().out
    assert (
        captured_out
        == (
            "foo\n"  # from `b_sink.consume(c)`
            "bar\n"  # from `b_sink.consume(c)`
        )
    )

    with_some_c_sink(ConcreteCSink())
    captured_out = capsys.readouterr().out
    assert (
        captured_out
        == (
            "foo\n"  # from `c_sink.consume(c)`
            "bar\n"  # from `c_sink.consume(c)`
            "baz\n"  # from `c_sink.consume(c)`
        )
    )
