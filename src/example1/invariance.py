from typing import Callable

from .world import A, B, C, D, consume_a, consume_b, consume_c, consume_d, produce_a, produce_b, produce_c, produce_d


def delegate_consume_a_and_produce_a(consume_a_and_produce_a: Callable[[A], A]) -> None:
    a = produce_a()
    new_a = consume_a_and_produce_a(a)
    consume_a(new_a)


def delegate_consume_b_and_produce_b(consume_b_and_produce_b: Callable[[B], B]) -> None:
    b = produce_b()
    new_b = consume_b_and_produce_b(b)
    consume_b(new_b)


def delegate_consume_c_and_produce_c(consume_c_and_produce_c: Callable[[C], C]) -> None:
    c = produce_c()
    new_c = consume_c_and_produce_c(c)
    consume_c(new_c)


def delegate_consume_d_and_produce_d(consume_d_and_produce_d: Callable[[D], D]) -> None:
    d = produce_d()
    new_d = consume_d_and_produce_d(d)
    consume_d(new_d)
