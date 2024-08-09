import pytest

from variance.contravariance import (
    PureASink,
    PureBSink,
    PureCSink,
    with_some_a_sink,
    with_some_b_sink,
    with_some_c_sink,
)


def test_with_some_a_sink(capsys: pytest.CaptureFixture[str]) -> None:
    a_sink, b_sink, c_sink = PureASink(), PureBSink(), PureCSink()  # noqa: F841

    with_some_a_sink(a_sink)

    captured_out = capsys.readouterr().out
    assert (
        captured_out
        == (
            "doing consume from PureASink\n"  #
            "doing foo from A\n"
            "doing consume from PureASink\n"
            "doing foo from B\n"
            "doing consume from PureASink\n"
            "doing foo from C\n"
        )
    )

    # with_some_a_sink(b_sink)

    # with_some_a_sink(c_sink)


def test_with_some_b_sink(capsys: pytest.CaptureFixture[str]) -> None:
    a_sink, b_sink, c_sink = PureASink(), PureBSink(), PureCSink()  # noqa: F841

    with_some_b_sink(a_sink)

    captured_out = capsys.readouterr().out
    assert (
        captured_out
        == (
            "doing consume from PureASink\n"  #
            "doing foo from B\n"
            "doing consume from PureASink\n"
            "doing foo from C\n"
        )
    )

    with_some_b_sink(b_sink)

    captured_out = capsys.readouterr().out
    assert (
        captured_out
        == (
            "doing consume from PureBSink\n"  #
            "doing foo from B\n"
            "doing bar from B\n"
            "doing consume from PureBSink\n"
            "doing foo from C\n"
            "doing bar from C\n"
        )
    )

    # with_some_b_sink(c_sink)


def test_with_some_c_sink(capsys: pytest.CaptureFixture[str]) -> None:
    a_sink, b_sink, c_sink = PureASink(), PureBSink(), PureCSink()

    with_some_c_sink(a_sink)

    captured_out = capsys.readouterr().out
    assert (
        captured_out
        == (
            "doing consume from PureASink\n"  #
            "doing foo from C\n"
        )
    )

    with_some_c_sink(b_sink)

    captured_out = capsys.readouterr().out
    assert (
        captured_out
        == (
            "doing consume from PureBSink\n"  #
            "doing foo from C\n"
            "doing bar from C\n"
        )
    )

    with_some_c_sink(c_sink)

    captured_out = capsys.readouterr().out
    assert (
        captured_out
        == (
            "doing consume from PureCSink\n"  #
            "doing foo from C\n"
            "doing bar from C\n"
            "doing baz from C\n"
        )
    )
