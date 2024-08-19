from typing import Callable

from typing_extensions import TypeAlias

from example1.world import (
    A,
    B,
    C,
    D,
    consume_a,
    consume_and_produce_a,
    consume_and_produce_b,
    consume_and_produce_c,
    consume_and_produce_d,
    consume_b,
    consume_c,
    consume_d,
    produce_a,
    produce_b,
    produce_c,
    produce_d,
)

ConsumeAndProduceAFn: TypeAlias = Callable[[A], A]
ConsumeAndProduceBFn: TypeAlias = Callable[[B], B]
ConsumeAndProduceCFn: TypeAlias = Callable[[C], C]
ConsumeAndProduceDFn: TypeAlias = Callable[[D], D]


def with_consume_and_produce_a_fn(consume_and_produce_a_fn: ConsumeAndProduceAFn, a: A) -> A:
    new_a = consume_and_produce_a_fn(a)
    return new_a


def with_consume_and_produce_b_fn(consume_and_produce_b_fn: ConsumeAndProduceBFn, b: B) -> B:
    new_b = consume_and_produce_b_fn(b)
    return new_b


def with_consume_and_produce_c_fn(consume_and_produce_c_fn: ConsumeAndProduceCFn, c: C) -> C:
    new_c = consume_and_produce_c_fn(c)
    return new_c


def with_consume_and_produce_d_fn(consume_and_produce_d_fn: ConsumeAndProduceDFn, d: D) -> D:
    new_d = consume_and_produce_d_fn(d)
    return new_d


consume_a(with_consume_and_produce_a_fn(consume_and_produce_a, produce_a()))
consume_a(with_consume_and_produce_a_fn(consume_and_produce_a, produce_b()))
consume_a(with_consume_and_produce_a_fn(consume_and_produce_a, produce_c()))
consume_a(with_consume_and_produce_a_fn(consume_and_produce_a, produce_d()))

consume_b(with_consume_and_produce_a_fn(consume_and_produce_a, produce_a()))
consume_b(with_consume_and_produce_a_fn(consume_and_produce_a, produce_b()))
consume_b(with_consume_and_produce_a_fn(consume_and_produce_a, produce_c()))
consume_b(with_consume_and_produce_a_fn(consume_and_produce_a, produce_d()))

consume_c(with_consume_and_produce_a_fn(consume_and_produce_a, produce_a()))
consume_c(with_consume_and_produce_a_fn(consume_and_produce_a, produce_b()))
consume_c(with_consume_and_produce_a_fn(consume_and_produce_a, produce_c()))
consume_c(with_consume_and_produce_a_fn(consume_and_produce_a, produce_d()))

consume_d(with_consume_and_produce_a_fn(consume_and_produce_a, produce_a()))
consume_d(with_consume_and_produce_a_fn(consume_and_produce_a, produce_b()))
consume_d(with_consume_and_produce_a_fn(consume_and_produce_a, produce_c()))
consume_d(with_consume_and_produce_a_fn(consume_and_produce_a, produce_d()))

consume_a(with_consume_and_produce_b_fn(consume_and_produce_a, produce_a()))
consume_a(with_consume_and_produce_b_fn(consume_and_produce_a, produce_b()))
consume_a(with_consume_and_produce_b_fn(consume_and_produce_a, produce_c()))
consume_a(with_consume_and_produce_b_fn(consume_and_produce_a, produce_d()))

consume_b(with_consume_and_produce_b_fn(consume_and_produce_a, produce_a()))
consume_b(with_consume_and_produce_b_fn(consume_and_produce_a, produce_b()))
consume_b(with_consume_and_produce_b_fn(consume_and_produce_a, produce_c()))
consume_b(with_consume_and_produce_b_fn(consume_and_produce_a, produce_d()))

consume_c(with_consume_and_produce_b_fn(consume_and_produce_a, produce_a()))
consume_c(with_consume_and_produce_b_fn(consume_and_produce_a, produce_b()))
consume_c(with_consume_and_produce_b_fn(consume_and_produce_a, produce_c()))
consume_c(with_consume_and_produce_b_fn(consume_and_produce_a, produce_d()))

consume_d(with_consume_and_produce_b_fn(consume_and_produce_a, produce_a()))
consume_d(with_consume_and_produce_b_fn(consume_and_produce_a, produce_b()))
consume_d(with_consume_and_produce_b_fn(consume_and_produce_a, produce_c()))
consume_d(with_consume_and_produce_b_fn(consume_and_produce_a, produce_d()))

consume_a(with_consume_and_produce_c_fn(consume_and_produce_a, produce_a()))
consume_a(with_consume_and_produce_c_fn(consume_and_produce_a, produce_b()))
consume_a(with_consume_and_produce_c_fn(consume_and_produce_a, produce_c()))
consume_a(with_consume_and_produce_c_fn(consume_and_produce_a, produce_d()))

consume_b(with_consume_and_produce_c_fn(consume_and_produce_a, produce_a()))
consume_b(with_consume_and_produce_c_fn(consume_and_produce_a, produce_b()))
consume_b(with_consume_and_produce_c_fn(consume_and_produce_a, produce_c()))
consume_b(with_consume_and_produce_c_fn(consume_and_produce_a, produce_d()))

consume_c(with_consume_and_produce_c_fn(consume_and_produce_a, produce_a()))
consume_c(with_consume_and_produce_c_fn(consume_and_produce_a, produce_b()))
consume_c(with_consume_and_produce_c_fn(consume_and_produce_a, produce_c()))
consume_c(with_consume_and_produce_c_fn(consume_and_produce_a, produce_d()))

consume_d(with_consume_and_produce_c_fn(consume_and_produce_a, produce_a()))
consume_d(with_consume_and_produce_c_fn(consume_and_produce_a, produce_b()))
consume_d(with_consume_and_produce_c_fn(consume_and_produce_a, produce_c()))
consume_d(with_consume_and_produce_c_fn(consume_and_produce_a, produce_d()))

consume_a(with_consume_and_produce_d_fn(consume_and_produce_a, produce_a()))
consume_a(with_consume_and_produce_d_fn(consume_and_produce_a, produce_b()))
consume_a(with_consume_and_produce_d_fn(consume_and_produce_a, produce_c()))
consume_a(with_consume_and_produce_d_fn(consume_and_produce_a, produce_d()))

consume_b(with_consume_and_produce_d_fn(consume_and_produce_a, produce_a()))
consume_b(with_consume_and_produce_d_fn(consume_and_produce_a, produce_b()))
consume_b(with_consume_and_produce_d_fn(consume_and_produce_a, produce_c()))
consume_b(with_consume_and_produce_d_fn(consume_and_produce_a, produce_d()))

consume_c(with_consume_and_produce_d_fn(consume_and_produce_a, produce_a()))
consume_c(with_consume_and_produce_d_fn(consume_and_produce_a, produce_b()))
consume_c(with_consume_and_produce_d_fn(consume_and_produce_a, produce_c()))
consume_c(with_consume_and_produce_d_fn(consume_and_produce_a, produce_d()))

consume_d(with_consume_and_produce_d_fn(consume_and_produce_a, produce_a()))
consume_d(with_consume_and_produce_d_fn(consume_and_produce_a, produce_b()))
consume_d(with_consume_and_produce_d_fn(consume_and_produce_a, produce_c()))
consume_d(with_consume_and_produce_d_fn(consume_and_produce_a, produce_d()))


consume_a(with_consume_and_produce_a_fn(consume_and_produce_b, produce_a()))
consume_a(with_consume_and_produce_a_fn(consume_and_produce_b, produce_b()))
consume_a(with_consume_and_produce_a_fn(consume_and_produce_b, produce_c()))
consume_a(with_consume_and_produce_a_fn(consume_and_produce_b, produce_d()))

consume_b(with_consume_and_produce_a_fn(consume_and_produce_b, produce_a()))
consume_b(with_consume_and_produce_a_fn(consume_and_produce_b, produce_b()))
consume_b(with_consume_and_produce_a_fn(consume_and_produce_b, produce_c()))
consume_b(with_consume_and_produce_a_fn(consume_and_produce_b, produce_d()))

consume_c(with_consume_and_produce_a_fn(consume_and_produce_b, produce_a()))
consume_c(with_consume_and_produce_a_fn(consume_and_produce_b, produce_b()))
consume_c(with_consume_and_produce_a_fn(consume_and_produce_b, produce_c()))
consume_c(with_consume_and_produce_a_fn(consume_and_produce_b, produce_d()))

consume_d(with_consume_and_produce_a_fn(consume_and_produce_b, produce_a()))
consume_d(with_consume_and_produce_a_fn(consume_and_produce_b, produce_b()))
consume_d(with_consume_and_produce_a_fn(consume_and_produce_b, produce_c()))
consume_d(with_consume_and_produce_a_fn(consume_and_produce_b, produce_d()))

consume_a(with_consume_and_produce_b_fn(consume_and_produce_b, produce_a()))
consume_a(with_consume_and_produce_b_fn(consume_and_produce_b, produce_b()))
consume_a(with_consume_and_produce_b_fn(consume_and_produce_b, produce_c()))
consume_a(with_consume_and_produce_b_fn(consume_and_produce_b, produce_d()))

consume_b(with_consume_and_produce_b_fn(consume_and_produce_b, produce_a()))
consume_b(with_consume_and_produce_b_fn(consume_and_produce_b, produce_b()))
consume_b(with_consume_and_produce_b_fn(consume_and_produce_b, produce_c()))
consume_b(with_consume_and_produce_b_fn(consume_and_produce_b, produce_d()))

consume_c(with_consume_and_produce_b_fn(consume_and_produce_b, produce_a()))
consume_c(with_consume_and_produce_b_fn(consume_and_produce_b, produce_b()))
consume_c(with_consume_and_produce_b_fn(consume_and_produce_b, produce_c()))
consume_c(with_consume_and_produce_b_fn(consume_and_produce_b, produce_d()))

consume_d(with_consume_and_produce_b_fn(consume_and_produce_b, produce_a()))
consume_d(with_consume_and_produce_b_fn(consume_and_produce_b, produce_b()))
consume_d(with_consume_and_produce_b_fn(consume_and_produce_b, produce_c()))
consume_d(with_consume_and_produce_b_fn(consume_and_produce_b, produce_d()))

consume_a(with_consume_and_produce_c_fn(consume_and_produce_b, produce_a()))
consume_a(with_consume_and_produce_c_fn(consume_and_produce_b, produce_b()))
consume_a(with_consume_and_produce_c_fn(consume_and_produce_b, produce_c()))
consume_a(with_consume_and_produce_c_fn(consume_and_produce_b, produce_d()))

consume_b(with_consume_and_produce_c_fn(consume_and_produce_b, produce_a()))
consume_b(with_consume_and_produce_c_fn(consume_and_produce_b, produce_b()))
consume_b(with_consume_and_produce_c_fn(consume_and_produce_b, produce_c()))
consume_b(with_consume_and_produce_c_fn(consume_and_produce_b, produce_d()))

consume_c(with_consume_and_produce_c_fn(consume_and_produce_b, produce_a()))
consume_c(with_consume_and_produce_c_fn(consume_and_produce_b, produce_b()))
consume_c(with_consume_and_produce_c_fn(consume_and_produce_b, produce_c()))
consume_c(with_consume_and_produce_c_fn(consume_and_produce_b, produce_d()))

consume_d(with_consume_and_produce_c_fn(consume_and_produce_b, produce_a()))
consume_d(with_consume_and_produce_c_fn(consume_and_produce_b, produce_b()))
consume_d(with_consume_and_produce_c_fn(consume_and_produce_b, produce_c()))
consume_d(with_consume_and_produce_c_fn(consume_and_produce_b, produce_d()))

consume_a(with_consume_and_produce_d_fn(consume_and_produce_b, produce_a()))
consume_a(with_consume_and_produce_d_fn(consume_and_produce_b, produce_b()))
consume_a(with_consume_and_produce_d_fn(consume_and_produce_b, produce_c()))
consume_a(with_consume_and_produce_d_fn(consume_and_produce_b, produce_d()))

consume_b(with_consume_and_produce_d_fn(consume_and_produce_b, produce_a()))
consume_b(with_consume_and_produce_d_fn(consume_and_produce_b, produce_b()))
consume_b(with_consume_and_produce_d_fn(consume_and_produce_b, produce_c()))
consume_b(with_consume_and_produce_d_fn(consume_and_produce_b, produce_d()))

consume_c(with_consume_and_produce_d_fn(consume_and_produce_b, produce_a()))
consume_c(with_consume_and_produce_d_fn(consume_and_produce_b, produce_b()))
consume_c(with_consume_and_produce_d_fn(consume_and_produce_b, produce_c()))
consume_c(with_consume_and_produce_d_fn(consume_and_produce_b, produce_d()))

consume_d(with_consume_and_produce_d_fn(consume_and_produce_b, produce_a()))
consume_d(with_consume_and_produce_d_fn(consume_and_produce_b, produce_b()))
consume_d(with_consume_and_produce_d_fn(consume_and_produce_b, produce_c()))
consume_d(with_consume_and_produce_d_fn(consume_and_produce_b, produce_d()))


consume_a(with_consume_and_produce_a_fn(consume_and_produce_c, produce_a()))
consume_a(with_consume_and_produce_a_fn(consume_and_produce_c, produce_b()))
consume_a(with_consume_and_produce_a_fn(consume_and_produce_c, produce_c()))
consume_a(with_consume_and_produce_a_fn(consume_and_produce_c, produce_d()))

consume_b(with_consume_and_produce_a_fn(consume_and_produce_c, produce_a()))
consume_b(with_consume_and_produce_a_fn(consume_and_produce_c, produce_b()))
consume_b(with_consume_and_produce_a_fn(consume_and_produce_c, produce_c()))
consume_b(with_consume_and_produce_a_fn(consume_and_produce_c, produce_d()))

consume_c(with_consume_and_produce_a_fn(consume_and_produce_c, produce_a()))
consume_c(with_consume_and_produce_a_fn(consume_and_produce_c, produce_b()))
consume_c(with_consume_and_produce_a_fn(consume_and_produce_c, produce_c()))
consume_c(with_consume_and_produce_a_fn(consume_and_produce_c, produce_d()))

consume_d(with_consume_and_produce_a_fn(consume_and_produce_c, produce_a()))
consume_d(with_consume_and_produce_a_fn(consume_and_produce_c, produce_b()))
consume_d(with_consume_and_produce_a_fn(consume_and_produce_c, produce_c()))
consume_d(with_consume_and_produce_a_fn(consume_and_produce_c, produce_d()))

consume_a(with_consume_and_produce_b_fn(consume_and_produce_c, produce_a()))
consume_a(with_consume_and_produce_b_fn(consume_and_produce_c, produce_b()))
consume_a(with_consume_and_produce_b_fn(consume_and_produce_c, produce_c()))
consume_a(with_consume_and_produce_b_fn(consume_and_produce_c, produce_d()))

consume_b(with_consume_and_produce_b_fn(consume_and_produce_c, produce_a()))
consume_b(with_consume_and_produce_b_fn(consume_and_produce_c, produce_b()))
consume_b(with_consume_and_produce_b_fn(consume_and_produce_c, produce_c()))
consume_b(with_consume_and_produce_b_fn(consume_and_produce_c, produce_d()))

consume_c(with_consume_and_produce_b_fn(consume_and_produce_c, produce_a()))
consume_c(with_consume_and_produce_b_fn(consume_and_produce_c, produce_b()))
consume_c(with_consume_and_produce_b_fn(consume_and_produce_c, produce_c()))
consume_c(with_consume_and_produce_b_fn(consume_and_produce_c, produce_d()))

consume_d(with_consume_and_produce_b_fn(consume_and_produce_c, produce_a()))
consume_d(with_consume_and_produce_b_fn(consume_and_produce_c, produce_b()))
consume_d(with_consume_and_produce_b_fn(consume_and_produce_c, produce_c()))
consume_d(with_consume_and_produce_b_fn(consume_and_produce_c, produce_d()))

consume_a(with_consume_and_produce_c_fn(consume_and_produce_c, produce_a()))
consume_a(with_consume_and_produce_c_fn(consume_and_produce_c, produce_b()))
consume_a(with_consume_and_produce_c_fn(consume_and_produce_c, produce_c()))
consume_a(with_consume_and_produce_c_fn(consume_and_produce_c, produce_d()))

consume_b(with_consume_and_produce_c_fn(consume_and_produce_c, produce_a()))
consume_b(with_consume_and_produce_c_fn(consume_and_produce_c, produce_b()))
consume_b(with_consume_and_produce_c_fn(consume_and_produce_c, produce_c()))
consume_b(with_consume_and_produce_c_fn(consume_and_produce_c, produce_d()))

consume_c(with_consume_and_produce_c_fn(consume_and_produce_c, produce_a()))
consume_c(with_consume_and_produce_c_fn(consume_and_produce_c, produce_b()))
consume_c(with_consume_and_produce_c_fn(consume_and_produce_c, produce_c()))
consume_c(with_consume_and_produce_c_fn(consume_and_produce_c, produce_d()))

consume_d(with_consume_and_produce_c_fn(consume_and_produce_c, produce_a()))
consume_d(with_consume_and_produce_c_fn(consume_and_produce_c, produce_b()))
consume_d(with_consume_and_produce_c_fn(consume_and_produce_c, produce_c()))
consume_d(with_consume_and_produce_c_fn(consume_and_produce_c, produce_d()))

consume_a(with_consume_and_produce_d_fn(consume_and_produce_c, produce_a()))
consume_a(with_consume_and_produce_d_fn(consume_and_produce_c, produce_b()))
consume_a(with_consume_and_produce_d_fn(consume_and_produce_c, produce_c()))
consume_a(with_consume_and_produce_d_fn(consume_and_produce_c, produce_d()))

consume_b(with_consume_and_produce_d_fn(consume_and_produce_c, produce_a()))
consume_b(with_consume_and_produce_d_fn(consume_and_produce_c, produce_b()))
consume_b(with_consume_and_produce_d_fn(consume_and_produce_c, produce_c()))
consume_b(with_consume_and_produce_d_fn(consume_and_produce_c, produce_d()))

consume_c(with_consume_and_produce_d_fn(consume_and_produce_c, produce_a()))
consume_c(with_consume_and_produce_d_fn(consume_and_produce_c, produce_b()))
consume_c(with_consume_and_produce_d_fn(consume_and_produce_c, produce_c()))
consume_c(with_consume_and_produce_d_fn(consume_and_produce_c, produce_d()))

consume_d(with_consume_and_produce_d_fn(consume_and_produce_c, produce_a()))
consume_d(with_consume_and_produce_d_fn(consume_and_produce_c, produce_b()))
consume_d(with_consume_and_produce_d_fn(consume_and_produce_c, produce_c()))
consume_d(with_consume_and_produce_d_fn(consume_and_produce_c, produce_d()))


consume_a(with_consume_and_produce_a_fn(consume_and_produce_d, produce_a()))
consume_a(with_consume_and_produce_a_fn(consume_and_produce_d, produce_b()))
consume_a(with_consume_and_produce_a_fn(consume_and_produce_d, produce_c()))
consume_a(with_consume_and_produce_a_fn(consume_and_produce_d, produce_d()))

consume_b(with_consume_and_produce_a_fn(consume_and_produce_d, produce_a()))
consume_b(with_consume_and_produce_a_fn(consume_and_produce_d, produce_b()))
consume_b(with_consume_and_produce_a_fn(consume_and_produce_d, produce_c()))
consume_b(with_consume_and_produce_a_fn(consume_and_produce_d, produce_d()))

consume_c(with_consume_and_produce_a_fn(consume_and_produce_d, produce_a()))
consume_c(with_consume_and_produce_a_fn(consume_and_produce_d, produce_b()))
consume_c(with_consume_and_produce_a_fn(consume_and_produce_d, produce_c()))
consume_c(with_consume_and_produce_a_fn(consume_and_produce_d, produce_d()))

consume_d(with_consume_and_produce_a_fn(consume_and_produce_d, produce_a()))
consume_d(with_consume_and_produce_a_fn(consume_and_produce_d, produce_b()))
consume_d(with_consume_and_produce_a_fn(consume_and_produce_d, produce_c()))
consume_d(with_consume_and_produce_a_fn(consume_and_produce_d, produce_d()))

consume_a(with_consume_and_produce_b_fn(consume_and_produce_d, produce_a()))
consume_a(with_consume_and_produce_b_fn(consume_and_produce_d, produce_b()))
consume_a(with_consume_and_produce_b_fn(consume_and_produce_d, produce_c()))
consume_a(with_consume_and_produce_b_fn(consume_and_produce_d, produce_d()))

consume_b(with_consume_and_produce_b_fn(consume_and_produce_d, produce_a()))
consume_b(with_consume_and_produce_b_fn(consume_and_produce_d, produce_b()))
consume_b(with_consume_and_produce_b_fn(consume_and_produce_d, produce_c()))
consume_b(with_consume_and_produce_b_fn(consume_and_produce_d, produce_d()))

consume_c(with_consume_and_produce_b_fn(consume_and_produce_d, produce_a()))
consume_c(with_consume_and_produce_b_fn(consume_and_produce_d, produce_b()))
consume_c(with_consume_and_produce_b_fn(consume_and_produce_d, produce_c()))
consume_c(with_consume_and_produce_b_fn(consume_and_produce_d, produce_d()))

consume_d(with_consume_and_produce_b_fn(consume_and_produce_d, produce_a()))
consume_d(with_consume_and_produce_b_fn(consume_and_produce_d, produce_b()))
consume_d(with_consume_and_produce_b_fn(consume_and_produce_d, produce_c()))
consume_d(with_consume_and_produce_b_fn(consume_and_produce_d, produce_d()))

consume_a(with_consume_and_produce_c_fn(consume_and_produce_d, produce_a()))
consume_a(with_consume_and_produce_c_fn(consume_and_produce_d, produce_b()))
consume_a(with_consume_and_produce_c_fn(consume_and_produce_d, produce_c()))
consume_a(with_consume_and_produce_c_fn(consume_and_produce_d, produce_d()))

consume_b(with_consume_and_produce_c_fn(consume_and_produce_d, produce_a()))
consume_b(with_consume_and_produce_c_fn(consume_and_produce_d, produce_b()))
consume_b(with_consume_and_produce_c_fn(consume_and_produce_d, produce_c()))
consume_b(with_consume_and_produce_c_fn(consume_and_produce_d, produce_d()))

consume_c(with_consume_and_produce_c_fn(consume_and_produce_d, produce_a()))
consume_c(with_consume_and_produce_c_fn(consume_and_produce_d, produce_b()))
consume_c(with_consume_and_produce_c_fn(consume_and_produce_d, produce_c()))
consume_c(with_consume_and_produce_c_fn(consume_and_produce_d, produce_d()))

consume_d(with_consume_and_produce_c_fn(consume_and_produce_d, produce_a()))
consume_d(with_consume_and_produce_c_fn(consume_and_produce_d, produce_b()))
consume_d(with_consume_and_produce_c_fn(consume_and_produce_d, produce_c()))
consume_d(with_consume_and_produce_c_fn(consume_and_produce_d, produce_d()))

consume_a(with_consume_and_produce_d_fn(consume_and_produce_d, produce_a()))
consume_a(with_consume_and_produce_d_fn(consume_and_produce_d, produce_b()))
consume_a(with_consume_and_produce_d_fn(consume_and_produce_d, produce_c()))
consume_a(with_consume_and_produce_d_fn(consume_and_produce_d, produce_d()))

consume_b(with_consume_and_produce_d_fn(consume_and_produce_d, produce_a()))
consume_b(with_consume_and_produce_d_fn(consume_and_produce_d, produce_b()))
consume_b(with_consume_and_produce_d_fn(consume_and_produce_d, produce_c()))
consume_b(with_consume_and_produce_d_fn(consume_and_produce_d, produce_d()))

consume_c(with_consume_and_produce_d_fn(consume_and_produce_d, produce_a()))
consume_c(with_consume_and_produce_d_fn(consume_and_produce_d, produce_b()))
consume_c(with_consume_and_produce_d_fn(consume_and_produce_d, produce_c()))
consume_c(with_consume_and_produce_d_fn(consume_and_produce_d, produce_d()))

consume_d(with_consume_and_produce_d_fn(consume_and_produce_d, produce_a()))
consume_d(with_consume_and_produce_d_fn(consume_and_produce_d, produce_b()))
consume_d(with_consume_and_produce_d_fn(consume_and_produce_d, produce_c()))
consume_d(with_consume_and_produce_d_fn(consume_and_produce_d, produce_d()))
