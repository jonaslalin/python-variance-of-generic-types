from typing import Callable

from .world import A, B, C, D, consume_a, consume_b, consume_c, consume_d


def delegate_produce_a(produce_a: Callable[[], A]) -> None:
    a = produce_a()
    consume_a(a)


def delegate_produce_b(produce_b: Callable[[], B]) -> None:
    b = produce_b()
    consume_b(b)


def delegate_produce_c(produce_c: Callable[[], C]) -> None:
    c = produce_c()
    consume_c(c)


def delegate_produce_d(produce_d: Callable[[], D]) -> None:
    d = produce_d()
    consume_d(d)
