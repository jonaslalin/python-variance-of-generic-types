import pytest

from variance.contravariance import (
    PureAConsumer,
    PureBConsumer,
    PureCConsumer,
    with_some_a_consumer,
    with_some_b_consumer,
    with_some_c_consumer,
)


def test_with_some_a_consumer(capsys: pytest.CaptureFixture[str]) -> None:
    a_consumer, b_consumer, c_consumer = (
        PureAConsumer(),
        PureBConsumer(),
        PureCConsumer(),
    )  # noqa: F841

    with_some_a_consumer(a_consumer)

    captured_out = capsys.readouterr().out
    assert (
        captured_out
        == (
            "doing consume in PureAConsumer\n"  #
            "doing foo in A\n"
            "doing consume in PureAConsumer\n"
            "doing foo in B\n"
            "doing consume in PureAConsumer\n"
            "doing foo in C\n"
        )
    )

    # with_some_a_consumer(b_consumer)

    # with_some_a_consumer(c_consumer)


def test_with_some_b_consumer(capsys: pytest.CaptureFixture[str]) -> None:
    a_consumer, b_consumer, c_consumer = (
        PureAConsumer(),
        PureBConsumer(),
        PureCConsumer(),
    )  # noqa: F841

    with_some_b_consumer(a_consumer)

    captured_out = capsys.readouterr().out
    assert (
        captured_out
        == (
            "doing consume in PureAConsumer\n"  #
            "doing foo in B\n"
            "doing consume in PureAConsumer\n"
            "doing foo in C\n"
        )
    )

    with_some_b_consumer(b_consumer)

    captured_out = capsys.readouterr().out
    assert (
        captured_out
        == (
            "doing consume in PureBConsumer\n"  #
            "doing foo in B\n"
            "doing bar in B\n"
            "doing consume in PureBConsumer\n"
            "doing foo in C\n"
            "doing bar in C\n"
        )
    )

    # with_some_b_consumer(c_consumer)


def test_with_some_c_consumer(capsys: pytest.CaptureFixture[str]) -> None:
    a_consumer, b_consumer, c_consumer = (
        PureAConsumer(),
        PureBConsumer(),
        PureCConsumer(),
    )

    with_some_c_consumer(a_consumer)

    captured_out = capsys.readouterr().out
    assert (
        captured_out
        == (
            "doing consume in PureAConsumer\n"  #
            "doing foo in C\n"
        )
    )

    with_some_c_consumer(b_consumer)

    captured_out = capsys.readouterr().out
    assert (
        captured_out
        == (
            "doing consume in PureBConsumer\n"  #
            "doing foo in C\n"
            "doing bar in C\n"
        )
    )

    with_some_c_consumer(c_consumer)

    captured_out = capsys.readouterr().out
    assert (
        captured_out
        == (
            "doing consume in PureCConsumer\n"  #
            "doing foo in C\n"
            "doing bar in C\n"
            "doing baz in C\n"
        )
    )
