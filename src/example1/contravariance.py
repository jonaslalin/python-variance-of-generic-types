from typing import Callable

from .world import A, B, C, D, produce_a, produce_b, produce_c, produce_d


def delegate_consume_a(consume_a: Callable[[A], None]) -> None:
    a = produce_a()
    consume_a(a)


def delegate_consume_b(consume_b: Callable[[B], None]) -> None:
    b = produce_b()
    consume_b(b)


def delegate_consume_c(consume_c: Callable[[C], None]) -> None:
    c = produce_c()
    consume_c(c)


def delegate_consume_d(consume_d: Callable[[D], None]) -> None:
    d = produce_d()
    consume_d(d)
