import pytest

from variance.covariance import (
    ConcreteASource,
    ConcreteBSource,
    ConcreteCSource,
    with_some_a_source,
    with_some_b_source,
    with_some_c_source,
)


def test_with_some_a_source(capsys: pytest.CaptureFixture[str]) -> None:
    with_some_a_source(ConcreteASource())
    captured_out = capsys.readouterr().out
    assert captured_out == (
        "foo\n"  # from `a.foo()`
    )

    with_some_a_source(ConcreteBSource())
    captured_out = capsys.readouterr().out
    assert captured_out == (
        "foo\n"  # from `b.foo()`
    )

    with_some_a_source(ConcreteCSource())
    captured_out = capsys.readouterr().out
    assert captured_out == (
        "foo\n"  # from `c.foo()`
    )


def test_with_some_b_source(capsys: pytest.CaptureFixture[str]) -> None:
    # with_some_b_source(ConcreteASource())

    with_some_b_source(ConcreteBSource())
    captured_out = capsys.readouterr().out
    assert (
        captured_out
        == (
            "foo\n"  # from `b.foo()`
            "bar\n"  # from `b.bar()`
        )
    )

    with_some_b_source(ConcreteCSource())
    captured_out = capsys.readouterr().out
    assert (
        captured_out
        == (
            "foo\n"  # from `c.foo()`
            "bar\n"  # from `c.bar()`
        )
    )


def test_with_some_c_source(capsys: pytest.CaptureFixture[str]) -> None:
    # with_some_c_source(ConcreteASource())

    # with_some_c_source(ConcreteBSource())

    with_some_c_source(ConcreteCSource())
    captured_out = capsys.readouterr().out
    assert (
        captured_out
        == (
            "foo\n"  # from `c.foo()`
            "bar\n"  # from `c.bar()`
            "baz\n"  # from `c.baz()`
        )
    )
