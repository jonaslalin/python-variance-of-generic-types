import pytest

from variance.covariance import (
    PureAProducer,
    PureBProducer,
    PureCProducer,
    with_some_a_producer,
    with_some_b_producer,
    with_some_c_producer,
)


def test_with_some_a_producer(capsys: pytest.CaptureFixture[str]) -> None:
    a_producer, b_producer, c_producer = (
        PureAProducer(),
        PureBProducer(),
        PureCProducer(),
    )

    with_some_a_producer(a_producer)

    captured_out = capsys.readouterr().out
    assert (
        captured_out
        == (
            "doing produce in PureAProducer\n"  #
            "doing foo in A\n"
        )
    )

    with_some_a_producer(b_producer)

    captured_out = capsys.readouterr().out
    assert (
        captured_out
        == (
            "doing produce in PureBProducer\n"  #
            "doing foo in B\n"
        )
    )

    with_some_a_producer(c_producer)

    captured_out = capsys.readouterr().out
    assert (
        captured_out
        == (
            "doing produce in PureCProducer\n"  #
            "doing foo in C\n"
        )
    )


def test_with_some_b_producer(capsys: pytest.CaptureFixture[str]) -> None:
    a_producer, b_producer, c_producer = (  # noqa: F841
        PureAProducer(),
        PureBProducer(),
        PureCProducer(),
    )

    # with_some_b_producer(a_producer)

    with_some_b_producer(b_producer)

    captured_out = capsys.readouterr().out
    assert (
        captured_out
        == (
            "doing produce in PureBProducer\n"  #
            "doing foo in B\n"
            "doing bar in B\n"
        )
    )

    with_some_b_producer(c_producer)

    captured_out = capsys.readouterr().out
    assert (
        captured_out
        == (
            "doing produce in PureCProducer\n"  #
            "doing foo in C\n"
            "doing bar in C\n"
        )
    )


def test_with_some_c_producer(capsys: pytest.CaptureFixture[str]) -> None:
    a_producer, b_producer, c_producer = (  # noqa: F841
        PureAProducer(),
        PureBProducer(),
        PureCProducer(),
    )

    # with_some_c_producer(a_producer)

    # with_some_c_producer(b_producer)

    with_some_c_producer(c_producer)

    captured_out = capsys.readouterr().out
    assert (
        captured_out
        == (
            "doing produce in PureCProducer\n"  #
            "doing foo in C\n"
            "doing bar in C\n"
            "doing baz in C\n"
        )
    )
